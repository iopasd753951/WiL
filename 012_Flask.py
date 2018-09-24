# Sessions

# session은 cookie와 다르게 서버에 데이터가 저장된다.
# session은 클라이언트가 서버에 로그인하고 로그아웃하기까지의 시간 간격입니다.
# session통해 저장해야하는 데이터는 서버의 임시 디렉토리에 저장된다.

# session은 ["세션 변수" : 키 값]으로 구성된 dictionary 개체입니다.
import username as username
from flask import Flask, redirect, request, session, url_for
app = Flask(__name__)

session[username]='admin'
# username을 "세션 변수"로 설정함

session.pop('name', None)
# 세션변수를 해제 --> pop()으로 해제해줌ㅎ


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>

   '''