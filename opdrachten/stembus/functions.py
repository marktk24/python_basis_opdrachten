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


# define the get_candidate_vote function
def get_candidate_vote(candidate_name):
    request = requests.get(API_SOC + '/Candidate/' + candidate_name)
    answer = request.json()
    content = json.loads(answer)
    votes = content['votes']
    return votes


# define the add_candidate function
def add_candidate(candidate_name):
    request = requests.post(API_SOC + '/Candidate/' + candidate_name)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Candidate already exist':
        return 'Candidate already exist'
    else:
        return 'Something went wrong'


# define the change_candidate_votes function
def change_candidate_votes(candidate_name, votes):
    data = {'votes': int(votes)}
    request = requests.patch(API_SOC + '/Candidate/' + candidate_name, data)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Candidate does not exist':
        return 'Candidate does not exist'
    else:
        return 'Something went wrong'


# define the delete_candidate function
def delete_candidate(candidate_name):
    request = requests.delete(API_SOC + '/Candidate/' + candidate_name)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Candidate does not exist':
        return 'Candidate does not exist'
    else:
        return 'Something went wrong'


# define the get_voters function
def get_voters():
    request = requests.get(API_SOC + '/Voters')
    answer = request.json()
    content = json.loads(answer)
    voter_list = content['Voters']
    return voter_list


# define the get_voter_status function
def get_voter_status(voter_name):
    request = requests.get(API_SOC + '/Voter/' + voter_name)
    answer = request.json()
    content = json.loads(answer)
    status = content['status']
    return status


# define the add_voter function
def add_voter(voter_name):
    request = requests.post(API_SOC + '/Voter/' + voter_name)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Voter already exist':
        return 'Voter already exist'
    else:
        return 'Something went wrong'


# define the change_voter_status function
def change_voter_status(voter_name, status):
    data = {'status': bool(status)}
    request = requests.patch(API_SOC + '/Voter/' + voter_name, data)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Voter does not exist':
        return 'Voter does not exist'
    else:
        return 'Something went wrong'


# define the delete_candidate function
def delete_voter(voter_name):
    request = requests.delete(API_SOC + '/Voter/' + voter_name)
    answer = request.json()
    if answer['error'] is None:
        return None
    elif answer['error'] == 'Voter does not exist':
        return 'Voter does not exist'
    else:
        return 'Something went wrong'


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


# define the get_votes function
def get_votes():
    request = requests.get(API_SOC + '/Votes')
    answer = request.json()
    return answer
