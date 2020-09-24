from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getdata():
    comname = request.form['comname']
    return render_template('result.html', comname=comname)


if __name__ == "__main__":
    app.run(debug=True)