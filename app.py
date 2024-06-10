from flask import Flask, render_template, request, url_for, redirect, session
from sqlalchemy import text								
from config import os		
# from models import db, User, Email     
from models import db, User, UserAccount, Products , UserComments  


app = Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('nexusdb')
db.init_app(app)												

loggedin = False

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    # 
    if 'loggedin' in session and session['loggedin']:
        return render_template('index.html', username=session.get('username'))
    else:
        return render_template('index.html')

@app.route("/esports")
def esports():
     if 'loggedin' in session and session['loggedin']:
        return render_template('esports.html', username=session.get('username'))
     else:
        return render_template("esports.html")

@app.route("/news")
def news():
     if 'loggedin' in session and session['loggedin']:
        return render_template('news.html', username=session.get('username'))
     else:
        return render_template("news.html")

@app.route("/store")
def store():
     if 'loggedin' in session and session['loggedin']:
        return render_template('store.html', username=session.get('username'))
     else:
        return render_template("store.html")

@app.route("/contact")
def contact():
     if 'loggedin' in session and session['loggedin']:
        return render_template('contact.html', username=session.get('username'))
     else:
        return render_template("contact.html")

@app.route('/login')
def login():
        return render_template("login.html")

@app.route('/loginuser', methods=["POST"])
def loginuser():
    username = request.form.get("username")
    password = request.form.get("password")
    
    user_account = UserAccount.query.filter_by(username=username, password=password).first()
    
    if user_account:
        session['loggedin'] = True
        session['username'] = username
        return render_template("index.html", username=username, loggedin=True)
    else:
        return render_template("login.html")
    
@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return render_template("login.html")

@app.route('/deleteuser', methods=["GET", "POST"])
def deleteuser():
    username = session.get('username')
    
    # Find the user by username
    user = UserAccount.query.filter_by(username=username).first()
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('signup.html'))
    else:
        return "User not found", 404  # Not Found

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/register', methods=["POST"])
def register():
    print("Form data:", request.form)
    new_User = User(
        fname = request.form.get("fname"),
        lname = request.form.get("lname"),
        address = request.form.get("address")
    )
    
    db.session.add(new_User)
    
    new_UserAccount = UserAccount(
        # email = request.form.get("email"),
        username = request.form.get("username"),
        password = request.form.get("password")
        
    )
    
    db.session.add(new_UserAccount)
    db.session.commit()
    
    return redirect(url_for('login'))

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)
