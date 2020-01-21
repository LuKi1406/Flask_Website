from flask import Flask,request, render_template, url_for,make_response


app= Flask(__name__)


@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    
     return render_template('about.html')

@app.route('/faq',methods=['GET'])     
def faq():
    
     return render_template('faq.html')
@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    
    if request.method == 'POST':
        username = request.form["username"]
        passwd = request.form["passwd"]
        if username == 'you' and passwd == 'flask':
            msg = 'Username and password are correct'
        else:
            msg = 'Username or password are incorrect'
    return render_template('login.html', message=msg)


