from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Date', 'Time', 'Team', 'Language'}
    json_dump = json_dump(data_set)

    return json_dump

@app.route('/user', methods=['GET'])
def request_page():
    user_input = str(request.args.get('user'))

    data_set = {'Date', 'Time', 'Team', 'Language'}
    json_dump = json_dump(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7765)