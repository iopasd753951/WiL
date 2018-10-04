# Sessions

# session은 cookie와 다르게 서버에 데이터가 저장된다.
# session은 클라이언트가 서버에 로그인하고 로그아웃하기까지의 시간 간격입니다.
# session통해 저장해야하는 데이터는 서버의 임시 디렉토리에 저장된다.

# session은 ["세션 변수" : 키 값]으로 구성된 dictionary 개체이다.
import username as username
from flask import Flask, redirect, request, session, url_for
app = Flask(__name__)

# session[username] = 'admin'
# username을 "세션 변수"로 설정함

# session.pop('name', None)
# 세션변수를 해제 --> pop()으로 해제해줌


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']

        return 'Logged in as ' + username + '<br>' + \
               '<b><a href = \'/logout\'>click here to log out</a></b>'

    return 'You are not logged in <br><a href = \'/login\'></b>' + \
           "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

  <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p><input type = submit value = Login/></p>
   </form>'

   '''


@app.route('/logout')
def logout():
   # 세션에 사용자 이름이 있을 경우 삭제함.
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)