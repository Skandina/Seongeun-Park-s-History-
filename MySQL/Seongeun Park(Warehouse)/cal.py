from flask import Flask,request,jsonify, abort
from flaskext.mysql import MySQL
from datetime import date
import json

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATEBASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "warehouse"
app.config['MYSQL_DATEBASE_HOST'] = "localhost"
mysql.init_app(app)
conn = mysql.connect()
today = date.today()

@app.route('/products', methods=['GET','POST'])
def products():
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM products")
            result = cursor.fetchmany(int(limit))
            
            products_number = [] 

            for line in result:
                lineDict = {'id' : line[0], 'name':line[1],'price':line[2],'amount':line[3],
                        'created_at':line[4],'updated_at':line[5]}
                products_number.append(lineDict)
            return json.dumps(products_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM products")
            result = cursor.fetchall()
            products_number = []

            for line  in result:
                lineDict = {'id' : line[0],'name' : line[1],'price' :line[2],'amount': line[3],
                        'created_at':line[4],'updated_at': line[5]}
                products_number.append(lineDict)
   
            return json.dumps(products_number, indent=4, sort_keys=False, default=str)

    if request.method == 'POST':
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        amount = data["amount"]
        result = {"name" : name, "price":price, "amount":amount}

        if isinstance(name, str) and  isinstance(price, int) and isinstance(amount, int):
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products(products_name,price,amount) VALUES (%s, %s, %s)",(name,price,amount))
            conn.commit()
            return result, 201
        else:
            abort(404)

@app.route('/products/<int:id_number>', methods=['GET','DELETE','PUT'])
def projects_1(id_number):
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM products WHERE id=%s", id_number)
            result = cursor.fetchmany(int(limit))
            
            products_number = [] 

            for line in result:
                lineDict = {'id' : line[0], 'name':line[1],'price':line[2],'amount':line[3],
                        'created_at':line[4],'updated_at':line[5]}
                products_number.append(lineDict)
            return json.dumps(products_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM products WHERE id=%s", id_number)
            result = cursor.fetchall()
            products_number = []

            for line  in result:
                lineDict = {'id' : line[0],'name' : line[1],'price' :line[2],'amount': line[3],
                        'created_at':line[4],'updated_at': line[5]}
            products_number.append(lineDict)
   
            return json.dumps(products_number, indent=4, sort_keys=False, default=str)


    if request.method == 'DELETE':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=%s", id_number)
        conn.commit()
        result = cursor.fetchall()
        delete_number = []

        return "deleted" 

    if request.method == 'PUT':
        cursor = conn.cursor()
        data = request.get_json()
        price = data["price"]
        amount = data["amount"]
        today_date = today.strftime("%Y-%m-%d")
        cursor.execute("UPDATE products SET price=%s,amount=%s,updated_at=%s WHERE id=%s", (price,amount,today_date,id_number))
        cursor.execute("SELECT * FROM products WHERE id=%s", id_number)

        conn.commit()
        result = cursor.fetchall()

        updated_list = []
        for line in result:
            lineDict = { 'id' : line[0],'name' : line[1],'price' :line[2],'amount': line[3],
                'created_at':line[4],'updated_at': line[5]}
        updated_list.append(lineDict)
        return json.dumps(updated_list, indent=4, sort_keys=False, default=str)


#customer

@app.route('/customers', methods=['GET','POST'])
def customers():
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM customers")
            result = cursor.fetchmany(int(limit))
            
            customers_number = [] 

            for line in result:
                lineDict = {'id' : line[0], 'first_name':line[1],'last_name':line[2],'street':line[3],
                        'postal_code':line[4], 'age':line[5],'created_at':line[6],'updated_at':line[7]}
                customers_number.append(lineDict)
            return json.dumps(customers_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM customers")
            result = cursor.fetchall()
            customers_number = []

            for line  in result:
                lineDict = {'id' : line[0],'first_name' : line[1],'last_name' :line[2],'street': line[3],
                        'postal_code':line[4],'age':line[5],'created_at':line[6],'updated_at': line[7]}
                customers_number.append(lineDict)
            return json.dumps(customers_number, indent=4, sort_keys=False, default=str)


    if request.method == 'POST':
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        street = data["street"]
        postal_code = data["postal_code"]
        age = data["age"]
        result = {"first_name" : first_name, "last_name":last_name, "street":street, "postal_code":postal_code, "age":age}

        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(street, str) and isinstance(postal_code, int) and isinstance(age, int):
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customers(first_name,last_name,street,postal_code,age) VALUES (%s, %s, %s, %s, %s)",(first_name,last_name,street,postal_code,age))
            conn.commit()
            return result, 201
        else:
            abort(404)

@app.route('/customers/<int:id_number>', methods=['GET','DELETE','PUT'])
def customer_1(id_number):
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM customers WHERE id=%s", id_number)
            result = cursor.fetchmany(int(limit))
            
            customers_number = [] 

            for line in result:
                lineDict = {'id' : line[0], 'first_name':line[1],'last_name':line[2],'street':line[3],
                        'postal_code':line[4], 'age':line[5],'created_at':line[6],'updated_at':line[7]}
                customers_number.append(lineDict)
            return json.dumps(customers_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM customers WHERE id=%s", id_number)
            result = cursor.fetchall()
            customers_number = []

            for line  in result:
                lineDict = {'id' : line[0],'first_name' : line[1],'last_name' :line[2],'street': line[3],
                        'postal_code':line[4],'age':line[5],'created_at':line[6],'updated_at': line[7]}
                customers_number.append(lineDict)
            return json.dumps(customers_number, indent=4, sort_keys=False, default=str)

    if request.method == 'DELETE':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id=%s", id_number)
        conn.commit()
        result = cursor.fetchall()
        delete_number = []

        return "deleted" 

    if request.method == 'PUT':
        cursor = conn.cursor()
        data = request.get_json()
        age = data["age"]
        today_date = today.strftime("%Y-%m-%d")
        cursor.execute("UPDATE customers SET age=%s,updated_at=%s WHERE id=%s", (age,today_date,id_number))
        cursor.execute("SELECT * FROM customers WHERE id=%s", id_number)
        conn.commit()
        result = cursor.fetchall()

        updated_list = []
        for line in result:
            lineDict = {'id':line[0], 'first_name':line[1], 'last_name':line[2], 'street':line[3], 'postal_code':line[4], 'age':line[5], 'created_at':line[6],'updated_at':line[7]}
            updated_list.append(lineDict)
        return json.dumps(updated_list, indent=4, sort_keys=False, default=str)

#staff

@app.route('/staff', methods=['GET','POST'])
def staff():
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM staff")
            result = cursor.fetchmany(int(limit))
            
            staff_number = [] 

            for line in result:
                lineDict = {'id' : line[0], 'first_name':line[1],'last_name':line[2],'employee_since':line[3],
                        'age':line[4],'created_at':line[5],'updated_at':line[6]}
                staff_number.append(lineDict)
            return json.dumps(staff_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM staff")
            result = cursor.fetchall()
            staff_number = []

            for line  in result:
                lineDict = {'id' : line[0], 'first_name':line[1],'last_name':line[2],'employee_since':line[3],
                        'age':line[4],'created_at':line[5],'updated_at':line[6]}
                staff_number.append(lineDict)
            return json.dumps(staff_number, indent=4, sort_keys=False, default=str)


    if request.method == 'POST':
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        employee_since = data["employee_since"]
        age = data["age"]
        result = {"first_name" : first_name, "last_name":last_name, "employee_since":employee_since, "age":age}

        cursor = conn.cursor()
        cursor.execute("INSERT INTO staff(first_name,last_name,employee_since,age) VALUES (%s, %s, %s, %s)",(first_name,last_name,employee_since,age))
        conn.commit()
        return result, 201

@app.route('/staff/<int:id_number>', methods=['GET','DELETE','PUT'])
def staff_1(id_number):
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM staff WHERE id=%s", id_number)
        result = cursor.fetchall()
        staff_number = []

        for line  in result:
             lineDict = {'id' : line[0],'first_name' : line[1],'last_name' : line[2],'employee_since': line[3],
                    'age': line[4], 'created_at':line[5],'updated_at': line[6]}
        staff_number.append(lineDict)
        return json.dumps(staff_number, indent=4, sort_keys=False, default=str)

    if request.method == 'DELETE':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM staff WHERE id=%s", id_number)
        conn.commit()
        result = cursor.fetchall()
        delete_number = []

        return "deleted" 

    if request.method == 'PUT':
        cursor = conn.cursor()
        data = request.get_json()
        age = data["age"]
        last_name = data["last_name"]
        today_date = today.strftime("%Y-%m-%d")
        cursor.execute("UPDATE staff SET age=%s, last_name=%s, updated_at=%s WHERE id=%s", (age,last_name,today_date,id_number))
        cursor.execute("SELECT * FROM staff WHERE id=%s", id_number)
        conn.commit()
        result = cursor.fetchall()

        updated_list = []
        for line in result:
            lineDict = {'id' : line[0],'first_name' : line[1],'last_name' : line[2],'employee_since': line[3],
                    'age': line[4], 'created_at':line[5],'updated_at': line[6]}
        updated_list.append(lineDict)
        return json.dumps(updated_list, indent=4, sort_keys=False, default=str)

#orders

@app.route('/orders', methods=['GET','POST'])
def orders():
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM orders")
            result = cursor.fetchmany(int(limit))
            
            orders_number = [] 

            for line in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM orders")
            result = cursor.fetchall()
            orders_number = []

            for line  in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

    if request.method == 'POST':
        data = request.get_json()
        products_id = data["products_id"]
        customers_id = data["customers_id"]
        staff_id = data["staff_id"]
        
        result = {"products_id" : products_id, "customers_id":customers_id, "staff_id":staff_id}

        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (products_id,customers_id,staff_id) VALUES (%s, %s, %s)",(products_id,customers_id,staff_id))
        conn.commit()
        return result, 201

#orders_1 

@app.route('/orders/<int:id_number>', methods=['GET'])
def orders_1(id_number):
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM orders WHERE products_id=%s", id_number)
            result = cursor.fetchmany(int(limit))
            
            orders_number = [] 

            for line in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM orders WHERE products_id=%s", id_number)
            result = cursor.fetchall()
            orders_number = []

            for line  in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

#orders_2

@app.route('/orders/<int:id_number1>/<int:id_number2>', methods =['GET','DELETE','PUT']) 
def orders_2(id_number1, id_number2):        
    if request.method == 'GET':
        cursor = conn.cursor()
        limit = request.args.get('limit')
        
        if limit is not None:
            cursor.execute("SELECT * FROM orders WHERE products_id=%s and customers_id=%s", (id_number1,id_number2))
            result = cursor.fetchmany(int(limit))
            
            orders_number = [] 

            for line in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

        else:
            cursor.execute("SELECT * FROM orders WHERE products_id=%s and customers_id=%s", (id_number1,id_number2))
            result = cursor.fetchall()
            orders_number = []

            for line  in result:
                lineDict = {'products_id':line[0], 'customers_id':line[1],'staff_id':line[2],
                        'created_at':line[3],'updated_at':line[4]}
                orders_number.append(lineDict)
            return json.dumps(orders_number, indent=4, sort_keys=False, default=str)

    if request.method == 'DELETE':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders  WHERE products_id=%s and customers_id=%s", (id_number1, id_number2))
        conn.commit()
        result = cursor.fetchall()
        delete_number = []

        return "deleted" 

    if request.method == 'PUT':
        cursor = conn.cursor()
        data = request.get_json()
        staff_id = data["staff_id"]
        today_date = today.strftime("%Y-%m-%d")
        cursor.execute("UPDATE orders SET staff_id=%s, updated_at=%s WHERE products_id=%s and customers_id=%s", (staff_id, today_date, id_number1, id_number2))
        cursor.execute("SELECT * FROM orders WHERE products_id=%s and customers_id=%s", (id_number1, id_number2))
        conn.commit()
        result = cursor.fetchall()

        updated_list = []
        for line in result:
            lineDict = {'products_id' : line[0],'customers_id' : line[1],'staff_id' : line[2],'created_at':line[3],'updated_at': line[4]}
            updated_list.append(lineDict)
        return json.dumps(updated_list, indent=4, sort_keys=False, default=str)


#def warehouse_select():
#    cursor = conn.cursor()
#    cursor.execute('SELECT * FROM products')
#    results = cursor.fetchall()
#    print(results)
#    return{}

#@app.route('/add', methods=["POST"])
#def add_1():
#    data = request.get_json()
#    num1 = data['num1']
 #   num2 = data['num2']
  #  if isinstance(num1, str) or isinstance(num2, str):
   #     abort(400)
   ## return {
    #        "num1" : num1,
     #       "num2" : num2,
      #      "operand" : "addition",
       #     "result" : num1 + num2
   # }

#@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
#def add_2(num1, num2):
#    return {
#            "num1" : num1,
#            "num2" : num2,
#            "operand" : "addition",
#            "result" : num1+num2
#    }


#@app.route('/sub/<int:num1>/<int:num2>')
#def sub(num1, num2):
#    res = num1 - num2
#    limit = request.args.get('limit')
#    if limit is not None:
#        if res < limit:
#            return {
#                "operand" : "subtract" , 
#                "num1" : num1,
#                "num2" : num2,
#                "result" : limit 
#                }
#    else:
#        return {
#                "operand" : "subtract",
#                "num1" : num1,
#                "num2" : num2,
#                "result" : res
#                }
#@app.route('/arrayify/<num>')
#def arrayify(num):
#    lista = list(num)
#    return jsonify(lista)

#@app.route('/postexample', methods=['POST'])
#def postexample():
#    json = request.get_json()
#    cursor = conn.cursor()
#    cursor.execute("SELECT * FROM products")
#    res = cursor.fetchall()
#    print(res)
#    return {}

    
if __name__ == "__main__":
    app.run(debug=True)
