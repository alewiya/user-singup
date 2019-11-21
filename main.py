from flask import Flask,request,render_template,redirect
app = Flask(__name__)
app.config['DEBUG'] = True    
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/index", methods=['POST'])
def signup():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']
    username_error=''
    password_error=''
    verify_error=''
    email_error=''
    if (username.isspace()==True) and (len(username) < 0):
        username_error="That's not a valid username"
        username=''
    else:
        if (password.isspace()==True) and int(len(password) < 3) and int(len(password)>20) and int(len(password)<0):
            password_error="That's not a valid password"
            password=''
    if verify != password:
        verify_error="That's do  not match"
        verify=''
    if int(len(email))>0:
        if "@" not in email and '.' not in email and " " not in email:
            email_error="That's not a valid email"
            email=''
        else:
            if int(len(email) <3 or int(len(email)>20)):
                email_error="That's not a valid email"
                email=''
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('homepage.html',username=username)
    
    return render_template('index.html',username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error,username=username,password=password,verify=verify,email=email)
@app.route('/homepage')
def greeting():
    username=request.args.get('username')
    return render_template('homepage.html',username=username)
app.run()