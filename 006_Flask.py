from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    # user()는 수신된 인수가 admin인지 여부를 확인하고 일치할 경우에는 redirect(hello_amdin)으로
    # request된다. guest로 값을 받으면 hello_guest() 함수로 리디렉션된다.
    if name == 'admin':
      return redirect(url_for('hello_admin'))
    else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':

   app.run(debug = True)