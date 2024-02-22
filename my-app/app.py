from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Flask докер-образ <h1>"


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("3000"), debug=True)
