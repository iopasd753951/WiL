from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')

# 별 의미 없는거 같다 /int:postID 는 뒤에 동적라우트는 주소가 상수만 가능하게 해준다.

def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug= True)