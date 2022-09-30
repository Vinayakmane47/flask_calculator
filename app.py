from flask import Flask, render_template, request, jsonify
import math

import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://Vinayak:Sak$103138@cluster0.j3xloau.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


db1 = client['mongotest']
coll = db1['calculations']


app = Flask(__name__)



@app.route('/calculate', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            output = {f"sum of {num1} and {num2}": r }

            coll.insert_one(output)

        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            output = {f"subtract of {num1} and {num2}": r }
            coll.insert_one(output)

        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            output = {f"Multiplication  of {num1} and {num2}": r }
            coll.insert_one(output)

        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            output = {f"division of {num1} and {num2}": r }
            coll.insert_one(output)
        return jsonify(result)


if __name__ == '__main__':
    app.run()