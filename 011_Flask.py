# Cookie

from flask import render_template, Flask, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')
# template에서 index2.html을 읽어옴


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
# nm을 readcookie.html에 저장? 함
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
# readcookie에서 getcookie에 대한 하이퍼링크를 포함하여 View로 표시함
    return '<h1>welcome '+name+'</h1>'


if __name__ == '__main__':
    app.run(debug=True)