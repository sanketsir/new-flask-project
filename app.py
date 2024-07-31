from flask import Flask,make_response,jsonify
from model import db
app = Flask(__name__)



@app.route('/api/products1',methods=['GET'])
def getAllProducts():  # put application's code here
    return make_response(jsonify({"products1":db}), 200)




print("Hello")
if __name__ == '__main__':
    app.run()
