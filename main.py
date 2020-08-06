from bottle import Bottle, response, request, template, static_file
import bleach
from database import VaxTraxDb
from interface import *
import json

app = Bottle()


@app.route('/')
def index():
    """Return Homepage"""
    return template('index')


@app.route('/new_vaccine')
def new_vaccine():
    """Return form to create new vaccine"""
    return template('new_vaccine')


@app.route('/search_vac')
def search_vac():
    """Return form to search for already existing vaccine"""
    return template('vaccine_search')


@app.route('/update_vaccine', method='POST')
def update_vaccine():
    """Return template for update operation with vaccine information prefilled
    @params: form request => vaccine name
    """
    name = cleaner(request.forms.get('name'))
    vaccine = get_vac(db, name)
    if not vaccine['name']:
        return template('failure')
    else: 
        return template('update_vaccine', vac=vaccine)


@app.route('/static/<filename:path>')
def static(filename):
    """static file server for templates"""
    return static_file(filename=filename, root='static')


@app.route('/vaccine', method='GET')
def get_vaccines():
    """API endpoint for returning all vaccines"""
    vaccines = list_vaccines(db)
    res = json.dumps(vaccines)
    response.content_type = 'application/json'
    return res


@app.route('/vaccine', method='POST')
def post_vaccine():
    """Create new vaccine record inside database
    @params: form request => vaccine name
    @params: form request => vaccine type
    @params: form request => vaccine stage
    @params: form request => vaccine info
    """
    vaccine = {
        "name": cleaner(request.forms.get('name')),
        "type": cleaner(request.forms.get('type')),
        "stage": cleaner(request.forms.get('stage')),
        "info": cleaner(request.forms.get('info'))
    }
    insert_vaccine(db, vaccine)
    return template('success')


@app.route('/update', method='POST')
def put_vaccine():
    """Update vaccine record inside database
    @params: form request => vaccine name
    @params: form request => vaccine type
    @params: form request => vaccine stage
    @params: form request => vaccine info
    """
    vac = {
        "name": cleaner(request.forms.get('name')),
        "type": cleaner(request.forms.get('type')),
        "stage": cleaner(request.forms.get('stage')),
        "info": cleaner(request.forms.get('info'))
    }
    upd8_vaccine(db, vac)
    return template('success')


@app.route('/quizOne', method='PUT')
def quiz_one():
    """API endpoint for posting quiz solutions for question type 1
    @params: form request => data list of answer objects
    """
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
    """API endpoint for posting quiz solutions for question type 2
    @params: form request => data list of answer objects
    """
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


@app.route('/quizAns', method='GET')
def quiz_ans():
    """Return quiz answers"""
    ans_1 = list_answers(db)
    ans_2 = list_quiztwoanswers(db)
    ans = {
        "four": ans_1,
        "two": ans_2
    }
    return template('quiz_ans', ans=ans)


def cleaner(text):
    """input sanitization for prevention against xss"""
    return bleach.clean(text)


if __name__ == '__main__':
    db = VaxTraxDb()
    app.run(debug=True)
