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
