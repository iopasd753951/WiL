# template은 동적 요청을 받아 드릴 때 쓴다.


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index0.html")


if __name__=='__main__':
    app.run(debug=True)