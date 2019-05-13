from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)


@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mogakko():
    mongo.db.mogakko.insert_one({'data': 'hello'})
    # TODO: handle HTTP requests to CRUD data from frontend
    return "HELLO"


if __name__ == '__main__':
    app.run()
