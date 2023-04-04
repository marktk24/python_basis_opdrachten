# admin.py

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


# define the get_votes function
def get_votes():
    request = requests.get(API_SOC + '/Votes')
    answer = request.json()
    return answer


# define the validate_input function
def validate_input(low: int, high: int, user_input):
    try:
        user_input = int(user_input)
        if not isinstance(user_input, int):
            return False
        elif user_input < low:
            return False
        elif user_input > high:
            return False
        else:
            return True
    except ValueError:
        return False


# create the GUI
print('Admin')
print('Socket = ' + API_SOC)
while True:
    print('1. Candidates')
    print('2. Voters')
    print('3. Result ')
    print('4. Exit')
    choice_head = input('Choose option: ')

    if validate_input(1, 4, choice_head):
        choice_head = int(choice_head)

        if choice_head == 1:
            while True:
                print('1. View candidates')
                print('2. Get candidate votes')
                print('3. Add candidate ')
                print('4. Change candidate votes')
                print('5. Delete candidate ')
                print('6. Back')
                choice_candidates = input('Choose option: ')

                if validate_input(1, 6, choice_candidates):
                    choice_candidates = int(choice_candidates)

                    if choice_candidates == 1:
                        print('____________________')

                        candidates = get_candidates()

                        a = 1
                        for candidate in candidates:
                            print(str(a) + ': ' + candidate)
                            a = a + 1

                        print('____________________')

                    elif choice_candidates == 2:
                        print('____________________')

                        candidates = get_candidates()

                        a = 1
                        for candidate in candidates:
                            print(str(a) + ': ' + candidate)
                            a = a + 1

                        choice_candidate_2 = input('Choose option: ')

                        if validate_input(1, len(candidates), choice_candidate_2):
                            choice_candidate_2 = int(choice_candidate_2)

                            choice_candidate_2 = choice_candidate_2 - 1
                            candidate_name = candidates[choice_candidate_2]
                            choice_candidate = get_candidate_vote(candidate_name)

                            print('____________________')
                            print(choice_candidate)
                            print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_candidates == 3:
                        print('____________________')

                        add_name: str = str(input('Name: '))
                        res = add_candidate(add_name)

                        if res is None:
                            print('____________________')
                            print('Success')
                            print('____________________')

                        else:
                            print('____________________')
                            print(res)
                            print('____________________')

                    elif choice_candidates == 4:
                        print('____________________')

                        candidates = get_candidates()

                        a = 1
                        for candidate in candidates:
                            print(str(a) + ': ' + candidate)
                            a = a + 1

                        choice_candidate_4 = input('Choose a candidate: ')

                        if validate_input(1, len(candidates), choice_candidate_4):
                            choice_candidate_4 = int(choice_candidate_4)

                            choice_candidate_4 = choice_candidate_4 - 1
                            candidate_name = candidates[choice_candidate_4]
                            new_vote = input('How many votes: ')

                            try:
                                new_vote = int(new_vote)

                                if isinstance(new_vote, int):
                                    res = change_candidate_votes(candidate_name, new_vote)

                                    if res is None:
                                        print('____________________')
                                        print('Success')
                                        print('____________________')

                                    else:
                                        print('____________________')
                                        print(res)
                                        print('____________________')

                                else:
                                    print('____________________')
                                    print('Not a value')
                                    print('____________________')

                            except TypeError:
                                print('____________________')
                                print('Not a option')
                                print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_candidates == 5:
                        print('____________________')

                        candidates = get_candidates()

                        a = 1
                        for candidate in candidates:
                            print(str(a) + ': ' + candidate)
                            a = a + 1

                        choice_candidate_5 = input('Choose a candidate: ')

                        if validate_input(1, len(candidates), choice_candidate_5):
                            choice_candidate_5 = int(choice_candidate_5)

                            choice_candidate_5 = choice_candidate_5 - 1
                            candidate_name = candidates[choice_candidate_5]
                            res = delete_candidate(candidate_name)

                            if res is None:
                                print('____________________')
                                print('Success')
                                print('____________________')

                            else:
                                print('____________________')
                                print(res)
                                print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_candidates == 6:
                        break

                else:
                    print('____________________')
                    print('Not a option')
                    print('____________________')

        elif choice_head == 2:
            while True:
                print('1. View voters')
                print('2. Get voter status')
                print('3. Add voter ')
                print('4. Change voter status')
                print('5. Delete voter ')
                print('6. Back')
                choice_voters = input('Choose option: ')

                if validate_input(1, 6, choice_voters):
                    choice_voters = int(choice_voters)

                    if choice_voters == 1:
                        print('____________________')

                        voters = get_voters()

                        a = 1
                        for voter in voters:
                            print(str(a) + ': ' + voter)
                            a = a + 1

                        print('____________________')

                    elif choice_voters == 2:
                        print('____________________')

                        voters = get_voters()

                        a = 1
                        for voter in voters:
                            print(str(a) + ': ' + voter)
                            a = a + 1

                        choice_voter_2 = input('Choose option: ')

                        if validate_input(1, len(voters), choice_voter_2):
                            choice_voter_2 = int(choice_voter_2)
                            choice_voter_2 = choice_voter_2 - 1

                            voter_name = voters[choice_voter_2]
                            choice_voter = get_voter_status(voter_name)

                            print('____________________')
                            print(choice_voter)
                            print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_voters == 3:
                        print('____________________')

                        add_name: str = str(input('Name: '))
                        res = add_voter(add_name)

                        if res is None:
                            print('____________________')
                            print('Success')
                            print('____________________')

                        else:
                            print('____________________')
                            print(res)
                            print('____________________')

                    elif choice_voters == 4:
                        print('____________________')

                        voters = get_voters()

                        a = 1
                        for voter in voters:
                            print(str(a) + ': ' + voter)
                            a = a + 1

                        choice_voter_4 = input('Choose option: ')

                        if validate_input(1, len(voters), choice_voter_4):
                            choice_voter_4 = int(choice_voter_4)

                            choice_voter_4 = choice_voter_4 - 1
                            voter_name = voters[choice_voter_4]
                            new_status = input('What is the new status: ')

                            if new_status == "True":
                                res = change_voter_status(voter_name, True)

                                if res is None:
                                    print('____________________')
                                    print('Success')
                                    print('____________________')

                                else:
                                    print('____________________')
                                    print(res)
                                    print('____________________')

                            elif new_status == "False":
                                res = change_voter_status(voter_name, False)

                                if res is None:
                                    print('____________________')
                                    print('Success')
                                    print('____________________')

                                else:
                                    print('____________________')
                                    print(res)
                                    print('____________________')

                            else:
                                print('____________________')
                                print('Not a correct value')
                                print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_voters == 5:
                        print('____________________')

                        voters = get_voters()

                        a = 1
                        for voter in voters:
                            print(str(a) + ': ' + voter)
                            a = a + 1

                        choice_voter_5 = input('Choose option: ')

                        if validate_input(1, len(voters), choice_voter_5):
                            choice_voter_5 = int(choice_voter_5)

                            choice_voter_5 = choice_voter_5 - 1
                            candidate_name = voters[choice_voter_5]
                            res = delete_voter(candidate_name)

                            if res is None:
                                print('____________________')
                                print('Success')
                                print('____________________')

                            else:
                                print('____________________')
                                print(res)
                                print('____________________')

                        else:
                            print('____________________')
                            print('Not a option')
                            print('____________________')

                    elif choice_voters == 6:
                        break

                else:
                    print('____________________')
                    print('Not a option')
                    print('____________________')

        elif choice_head == 3:
            print('____________________')

            vote_list = get_votes()
            vote_list_sorted = sorted(vote_list.items(), key=lambda x: x[1], reverse=True)
            vote_list_sorted = dict(vote_list_sorted)

            for item in vote_list_sorted:
                print(item + str(': ') + str(vote_list_sorted[item]))

            print('____________________')

        elif choice_head == 4:
            break

    else:
        print('____________________')
        print('Not a option')
        print('____________________')
