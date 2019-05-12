from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mogakko():
    return "HELLO"


if __name__ == '__main__':
    app.run()
