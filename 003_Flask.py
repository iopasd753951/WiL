from flask import Flask

app = Flask(__name__)


@app.route('/', method=['GET', 'POST'])
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(host, port, debug, options)

    # host = 기본값은 127.0.0.1이다. 서버를 외부에서 사용하기 위해서는 0.0.0.0으로 설정해야한다.
    # host = '0.0.0.0' 라고 써줘야 한다.

    # port = 기본값은 5000이다.
    # port = 8787 이라고 써준다.

    # debug = 기본값은 flase이다. true로 설정하면 디버그 정보를 제공한다. = 코드를 수정해도 자동으로 웹에 적용됨.
    # debug 만 써주면됨

    # options = 기본 Werkzeug서버로 전달됨.
