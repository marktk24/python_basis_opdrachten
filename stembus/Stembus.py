import PySimpleGUI as SG
import windows as wd
# import requests
try:
    import requests
except ImportError as e:
    print("requests is not installed")
    exit()


# import json
try:
    import json
except ImportError as e:
    print("json is not installed")
    exit()


# define the variables
API_SOC = "http://127.0.0.1:5000"


# define the get_candidates function
def get_candidates():
    request = requests.get(API_SOC + '/Candidates')
    answer = request.json()
    content = json.loads(answer)
    candidates_list = content['Candidates']
    return candidates_list


# define the get_voter_status function
def get_voter_status(voter_name):
    request = requests.get(API_SOC + '/Voter/' + voter_name)
    answer = request.json()
    content = json.loads(answer)
    status = content['status']
    return status


# define the vote function
def vote(voter_name, user_vote):
    data = {
        'voter_name': voter_name,
        'vote': user_vote
    }
    request = requests.post(API_SOC + '/Vote', data)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Cannot find candidate':
        return 'Cannot find candidate'
    elif answer['error'] == 'Voter cannot vote':
        return 'Voter cannot vote'
    elif answer['error'] == 'Voter does not exist':
        return 'Voter does not exist'
    else:
        return 'Something went wrong'


window1, window2, window3, window4, window5 = wd.make_window1(), None, None, None, None
window1.Maximize()

while True:
    window, event, values = SG.read_all_windows()
    if window == window1 and event in (SG.WIN_CLOSED, 'Stop'):
        break

    if window == window1:
        sn = values[0]
        if event == 'Volgende' and get_voter_status(sn) is False:
            window1.close()
            print(str(sn))

            candidates = get_candidates()
            window2 = wd.make_window2(candidates)
            window2.Maximize()
        else:
            window1.close()
            print(str(sn))
            window3 = wd.make_window3()
            window3.Maximize()

    if window == window2:
        stem = values[0]
        if event == 'Stem' and stem in get_candidates():
            window2.close()
            print(str(stem))

            error = vote(sn, stem)
            if error is None:
                window1 = wd.make_window1()
                window1.Maximize()
            else:
                window5 = wd.make_window5(error)
                window5.Maximize()

        else:
            window2.close()
            window4 = wd.make_window4()
            window4.Maximize()

    if window == window3:
        if event == 'Terug':
            window3.close()
            window1 = wd.make_window1()
            window1.Maximize()

    if window == window4:
        if event == 'Terug':
            window4.close()
            window2 = wd.make_window2(candidates)
            window2.Maximize()

    if window == window5:
        if event == 'Terug':
            window5.close()
            window1 = wd.make_window2(candidates)
            window1.Maximize()

window.close()
