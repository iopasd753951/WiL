from flask import Flask

app = Flask(__name__)

@app.route('/item/<code>')   # '/'만 쓰게되면 주소를 확장할 없지만 /<code>를 써주면서 확장하여 쓸 수 있다. == 동적 라우트
def item(code):
    return "<h1> %s </h1>" % code   # % code = 확장하는데 필요한 부분이다.

if __name__ == "__main__":
    app.run(debug=True)
