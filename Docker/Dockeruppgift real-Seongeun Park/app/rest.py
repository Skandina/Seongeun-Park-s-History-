import pymysql
from app import app
from db import mysql
from flask import jsonify,request

@app.route('/person', methods=['GET','POST'])
def users():

    if request.method == 'POST':
        data = request.get_json()
        person_id = data["id"]
        age = data["age"]
        name = data["name"]
        result = {"id" : person_id, "age":age, "name":name}

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO user(id,age,name) VALUES (%s, %s, %s)",(person_id,age,name))
        conn.commit()
        return result, 201 

    if request.method == 'GET':

        conn = mysql.connect()

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")

        rows = cursor.fetchall()

        resp = jsonify(rows)
        resp.status_code = 200

        return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

