from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def student():
    return render_template('Student.html')
# Student.html을 랜더링해서 보여줌


@app.route('/result', methods=['POST', 'GET'])
# post와 get으로 정보를 받음
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
