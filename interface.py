def list_vaccines(db):
    cursor = db.cursor()
    cursor.execute("""select * from vaccines""")
    vac_list = []
    for row in cursor:
        vac = {
            "name": row[0],
            "type": row[1],
            "stage": row[2],
            "info": row[3]
        }
        vac_list.append(vac)
    return vac_list


def get_vac(db, name):
    cursor = db.cursor()
    cursor.execute("""select * from vaccines where name=?""", (name,))
    vac = {
        "name": "",
        "type": "",
        "stage": "",
        "info": ""
    }
    for row in cursor:
        vac["name"] = row[0]
        vac["type"] = row[1]
        vac["stage"] = row[2]
        vac["info"] = row[3]
    return vac


def insert_vaccine(db, vac):
    cursor = db.cursor()
    query = "INSERT INTO vaccines (name, type, stage, info) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (vac["name"], vac["type"], vac["stage"], vac["info"]))
    db.commit()


def upd8_vaccine(db, vac):
    cursor = db.cursor()
    sql = """UPDATE vaccines SET type = ?, stage = ?, info = ? WHERE name = ?"""
    cursor.execute(sql, (vac['type'], vac['stage'], vac['info'], vac['name']))
    db.commit()
# methods for quizAnswers table


def list_answers(db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM quizAnswers""")
    ans_list = []
    for row in cursor:
        ans = {
            "question_id": row[0],
            "optionOne": row[1],
            "optionTwo": row[2],
            "optionThree": row[3],
            "optionFour": row[4]
        }
        ans_list.append(ans)
    return ans_list


def get_quizanswers(db, question_id):
    cursor = db.cursor()
    cursor.execute("""select * from quizAnswers where question_id=?""", (question_id,))
    ans = {
        "question_id": "",
        "optionOne": "",
        "optionTwo": "",
        "optionThree": "",
        "optionFour": ""
    }
    for row in cursor:
        ans["question_id"] = row[0]
        ans["optionOne"] = row[1]
        ans["optionTwo"] = row[2]
        ans["optionThree"] = row[3]
        ans["optionFour"] = row[4]
    return ans


def upd8_quizanswers(db, ans):
    cursor = db.cursor()
    sql = """UPDATE quizAnswers SET optionOne = ?, optionTwo = ?, optionThree = ?, optionFour = ? WHERE question_id = ?"""
    cursor.execute(sql, (ans['optionOne'], ans['optionTwo'], ans['optionThree'], ans['optionFour'], ans['question_id']))
    db.commit()

# methods for quizTwoAnswers


def list_quiztwoanswers(db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM quizTwoAnswers""")
    ans_list = []
    for row in cursor:
        anstwo = {
            "question_id": row[0],
            "optionOne": row[1],
            "optionTwo": row[2]
        }
        ans_list.append(anstwo)
    return ans_list


def get_quiztwoanswers(db, question_id):
    cursor = db.cursor()
    cursor.execute("""select * from quizTwoAnswers where question_id=?""", (question_id,))
    anstwo = {
        "question_id": "",
        "optionOne": "",
        "optionTwo": ""
    }
    for row in cursor:
        anstwo["question_id"] = row[0]
        anstwo["optionOne"] = row[1]
        anstwo["optionTwo"] = row[2]
    return anstwo


def upd8_quiztwoanswers(db, anstwo):
    cursor = db.cursor()
    sql = """UPDATE quizTwoAnswers SET optionOne = ?, optionTwo = ? WHERE question_id = ?"""
    cursor.execute(sql, (anstwo['optionOne'], anstwo['optionTwo'], anstwo['question_id']))
    db.commit()


