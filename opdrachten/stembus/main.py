# API

# import Flask
try:
    from flask import Flask, request
except ImportError:
    print("Flask is not installed")
    exit()

# import Flask-Restful
try:
    from flask_restful import Resource, Api
except ImportError:
    print("Flask-Restful is not installed")
    exit()

# import json
try:
    import json
except ImportError:
    print("json is not installed")
    exit()


# create a function to read the json file
def read_data_json():
    try:
        data_json = open('data.json')
    except FileNotFoundError:
        print("something went wrong reading data.json")
        exit()
    data_json = json.load(data_json)
    return data_json


# create a function to write the json file
def write_data_json(dictionary):
    value = json.dumps(dictionary)
    try:
        with open("data.json", "w") as writefile:
            writefile.write(value)
    except FileNotFoundError:
        print("something went wrong reading data.json")
        exit()


# create a function to get the candidates names
def get_candidate_names():
    data = read_data_json()['Candidates']
    names = []
    for name in data:
        names.append(name)
    return names


# create a function to get the candidate votes
def get_candidate_votes(candidate_name):
    data = read_data_json()['Candidates']
    candidates = get_candidate_names()
    if candidate_name in candidates:
        votes = int(data[candidate_name])
        return votes
    else:
        return None


# create a function to add a candidate
def add_candidate(candidate_name):
    candidates = get_candidate_names()
    if candidate_name not in candidates:
        data = read_data_json()
        data['Candidates'][candidate_name] = 0
        write_data_json(data)
    else:
        return 'Candidate already exist'


# create a function to change the candidate votes
def change_candidate(candidate_name, votes):
    data = read_data_json()
    candidates = get_candidate_names()
    if candidate_name in candidates:
        data['Candidates'][candidate_name] = int(votes)
        write_data_json(data)
    else:
        return 'Candidate does not exist'


# create a function to delete a candidate
def delete_candidate(candidate_name):
    data = read_data_json()
    candidates = get_candidate_names()
    if candidate_name in candidates:
        del data['Candidates'][candidate_name]
        write_data_json(data)
    else:
        return 'Candidate does not exist'


# create a function to get the voters names
def get_voter_names():
    data = read_data_json()['Voters']
    names = []
    for name in data:
        names.append(name)
    return names


# create a function to get the voter status
def get_voter_status(voter_name):
    data = read_data_json()['Voters']
    voters = get_voter_names()
    if voter_name in voters:
        status = bool(data[voter_name])
        return status
    else:
        return None


# create a function to add a voter
def add_voter(voter_name):
    voters = get_voter_names()
    if voter_name not in voters:
        data = read_data_json()
        data['Voters'][voter_name] = False
        write_data_json(data)
    else:
        return 'Voter already exist'


# create a function to change the voter status
def change_voter(voter_name, status):
    data = read_data_json()
    voters = get_voter_names()
    if voter_name in voters:
        if status == "True":
            data['Voters'][voter_name] = True
        elif status == "False":
            data['Voters'][voter_name] = False
        write_data_json(data)
    else:
        return 'Voter does not exist'


# create a function to delete a voter
def delete_voter(voter_name):
    data = read_data_json()
    voters = get_voter_names()
    if voter_name in voters:
        del data['Voters'][voter_name]
        write_data_json(data)
    else:
        return 'Voter does not exist'


# create a function to update the candidate votes
def update_voter_status(voter, status):
    data = read_data_json()
    voters = get_voter_names()
    if voter in voters:
        data['Voters'][voter] = bool(status)
        write_data_json(data)
    else:
        return 'error1'


# create a function to see all votes
def get_votes():
    data = read_data_json()['Candidates']
    return data


# create an app
app = Flask("VoteAPI")
api = Api(app)


# create the candidates class
class Candidates(Resource):
    @staticmethod
    def get():
        candidates = get_candidate_names()
        data = {
            "Candidates": candidates
        }
        js = json.dumps(data)
        return js


# create the candidate class
class Candidate(Resource):
    @staticmethod
    def get(candidate_name):
        votes = get_candidate_votes(candidate_name)
        data = {
            "votes": votes
        }
        js = json.dumps(data)
        return js

    @staticmethod
    def post(candidate_name):
        result = add_candidate(candidate_name)
        if result == 'Candidate already exist':
            return {'error': 'Candidate already exist'}
        else:
            return {'error': None}

    @staticmethod
    def patch(candidate_name):
        votes = request.form['votes']
        result = change_candidate(candidate_name, votes)
        if result is None:
            return {'error': None}
        elif result == 'Candidate does not exist':
            return {'error': 'Candidate does not exist'}
        else:
            return {'error': 'Something went wrong'}

    @staticmethod
    def delete(candidate_name):
        result = delete_candidate(candidate_name)
        if result is None:
            return {'error': None}
        elif result == 'Candidate does not exist':
            return {'error': 'Candidate does not exist'}
        else:
            return {'error': 'Something went wrong'}


# create the voters class
class Voters(Resource):
    @staticmethod
    def get():
        voters = get_voter_names()
        data = {
            "Voters": voters
        }
        js = json.dumps(data)
        return js


# create the Voter class
class Voter(Resource):
    @staticmethod
    def get(voter_name):
        status = get_voter_status(voter_name)
        data = {
            "status": status
        }
        js = json.dumps(data)
        return js

    @staticmethod
    def post(voter_name):
        result = add_voter(voter_name)
        if result == 'Voter already exist':
            return {'error': 'Voter already exist'}
        else:
            return {'error': None}

    @staticmethod
    def patch(voter_name):
        status = request.form['status']
        result = change_voter(voter_name, status)
        if result is None:
            return {'error': None}
        elif result == 'Voter does not exist':
            return {'error': 'Voter does not exist'}
        else:
            return {'error': 'Something went wrong'}

    @staticmethod
    def delete(voter_name):
        result = delete_voter(voter_name)
        if result is None:
            return {'error': None}
        elif result == 'Voter does not exist':
            return {'error': 'Voter does not exist'}
        else:
            return {'error': 'Something went wrong'}


# create the Vote class
class Vote(Resource):
    @staticmethod
    def post():
        voter_name = request.form['voter_name']
        vote = request.form['vote']
        status = get_voter_status(voter_name)
        if status is False:
            votes = get_candidate_votes(vote)
            if votes is not None:
                new_votes = votes + 1
                change_candidate(vote, int(new_votes))
                change_voter(voter_name, "True")
                return {'error': None}
            else:
                return {'error': 'Cannot find candidate'}
        elif status is True:
            return {'error': 'Voter cannot vote'}
        else:
            return {'error': 'Voter does not exist'}


# create the Votes class
class Votes(Resource):
    @staticmethod
    def get():
        return get_votes()


# add the API endpoints
api.add_resource(Candidates, "/Candidates")
api.add_resource(Candidate, "/Candidate/<candidate_name>")
api.add_resource(Voters, "/Voters")
api.add_resource(Voter, "/Voter/<voter_name>")
api.add_resource(Vote, "/Vote")
api.add_resource(Votes, "/Votes")

# run the application
if __name__ == '__main__':
    app.run(debug=True)
