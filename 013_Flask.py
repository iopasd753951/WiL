# redirect

# redirect는 redirect가 호출되면 응답 개체(response object)를 반환하고
# 지정된 상태 코드가 있는 다른 대상 위치로 사용자를 리디렉션한다.
# 즉, ('/')으로 들어갔을 때 다른 주소를 가르켜(direct) 줌


# redirect이 기본적으로 가지고 있는 명령어

# location : url에 응답을 리디렉션한다. (아마?)
# statuscode : 현재 상태를 브라우저 헤더에 보낸다. 기본 값은 302
# response : response는 요청을 인스턴스화 해줍니다.

from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('log_in.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
        # 로그인 실패 시 401코드 출력
   else:
      return redirect(url_for('index'))


@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
   app.run(debug = True)


