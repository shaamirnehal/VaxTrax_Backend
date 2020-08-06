from bottle import Bottle, response, request, template, static_file
from database import VaxTraxDb
from interface import *
import json

app = Bottle()


@app.route('/')
def index():
    return template('index')


@app.route('/new_vaccine')
def new_vaccine():
    return template('new_vaccine')


@app.route('/update_vaccine', method='POST')
def update_vaccine():
    name = request.forms.get('name')
    vaccine = get_vac(db, name)
    return template('update_vaccine', vac=vaccine)


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


@app.route('/vaccine', method='GET')
def get_vaccines():
    vaccines = list_vaccines(db)
    res = json.dumps(vaccines)
    response.content_type = 'application/json'
    return res


@app.route('/vaccine', method='POST')
def post_vaccine():
    vaccine = {
        "name": request.forms.get('name'),
        "type": request.forms.get('type'),
        "stage": request.forms.get('stage'),
        "info": request.forms.get('info')
    }
    insert_vaccine(db, vaccine)
    return '<b>Vaccine Added, redirect to <a href=/>Home</a></b>!'


@app.route('/update', method='POST')
def put_vaccine():
    vac = {
        "name": request.forms.get('name'),
        "type": request.forms.get('type'),
        "stage": request.forms.get('stage'),
        "info": request.forms.get('info')
    }
    upd8_vaccine(db, vac)
    return '<b>Vaccine Updated, redirect to <a href=/>Home</a></b>!'


@app.route('/quizOne', method='PUT')
def quiz_one():
    arr = request.forms.get('data')
    json_arr = json.loads(arr)
    for ans in json_arr:
        answer = {
            "question_id": ans["questionId"],
            "optionOne": ans["optionOne"],
            "optionTwo": ans["optionTwo"],
            "optionThree": ans["optionThree"],
            "optionFour": ans["optionFour"]
        }
        current = get_quizanswers(db, answer["question_id"])
        for key in answer:
            if answer[key] is True:
                current[key] += 1
                break
        upd8_quizanswers(db, current)


@app.route('/quizTwo', method='PUT')
def quiz_two():
    arr = request.forms.get('data')
    json_arr = json.loads(arr)
    for ans in json_arr:
        answer = {
            "question_id": ans["questionId"],
            "optionOne": ans["optionOne"],
            "optionTwo": ans["optionTwo"]
        }
        current = get_quiztwoanswers(db, answer["question_id"])
        for key in answer:
            if answer[key] is True:
                current[key] += 1
                break
        upd8_quiztwoanswers(db, current)


@app.route('/quizOne', method='GET')
def quiz_one():
    ans = list_answers(db)
    # ans_2 = list_quiztwoanswers(db)
    return template('quiz_one', ans=ans)


@app.route('/quizTwo', method='GET')
def quiz_one():
    ans = list_quiztwoanswers(db)
    return template('quiz_two', ans=ans)


if __name__ == '__main__':
    db = VaxTraxDb()
    app.run(debug=True)
