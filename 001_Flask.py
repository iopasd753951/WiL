from flask import Flask

app = Flask(__name__)       # 이부분까지는 플라스크를 사용하기전의 초기화 부분이다. = 기본설정

@app.route('/')              # app.route는 사용자가 웹 서버로 접근할 수는 있는 주소를 의미한다. ('/')최상위 주소를 의미한다.ㅎ
def hello_world():              # response부분이다. 이 코드는 사용자에게 response(전송)하는 일을 한다. 함수(hello_world)이름을 바꿔도 상관없다.
    return "<h1> Hello World </h1>"

if __name__ == "__main__":
    app.run(debug=True)