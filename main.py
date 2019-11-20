from flask import Flask, request,render_template
import html
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")
def index():
    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    return render_template('index.html')
app.run()
