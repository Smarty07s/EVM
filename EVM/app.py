from flask import *
from flask import request
from json import *

app = Flask(__name__)
user ='Hi'
count = 0



@app.route('/lgin',methods=['POST'])
# def check():
#     if request.method == 'POST':
#         result = request.form
#         if request.form['username'] == 'Admin' and request.form['password'] == '@3124':

#             return render_template("index.html",result = result)
#         else:
#             return render_template('login.html',err='Oops! an error occured')
#     else:
#         return render_template("login.html")

@app.route('/',methods=['GET','POST'])
def home(user=user):
    return render_template("index.html")


@app.route('/vote')
def vote():
    return render_template("vote.html")

app.run(debug=True,port=80)