from flask import Flask, render_template
from flask import request
import supporting_code

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getdata():
    comname = request.form['comname']
    s=supporting_code.hello()
    return render_template('result.html', comname=comname,s1=s[0],s2=s[1],s3=s[2],s4=s[3],s5=s[4],s6=s[5],s7=s[6],s8=s[7],s9=s[8],s10=s[9] )

@app.route('/news/', methods=['GET', 'POST'])
def news():
    return render_template('news.html')

@app.route('/aboutsm/', methods=['GET','POST'])
def aboutsm():
    return render_template('aboutsm.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route('/signup/', methods=['GET','POST'])
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)