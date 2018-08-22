from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


app.add_url_rule('/', 'hello', hello_world)
    # route와 같은 일을 한다.

if __name__ == "__main__":
    app.run()