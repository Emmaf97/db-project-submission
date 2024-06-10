from flask import Flask, render_template, request, url_for, redirect, session
from sqlalchemy import text								
from config import os		
# from models import db, User, Email     
from models import db, User, UserAccount, Products , UserComments  


app = Flask(__name__)
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

@app.route('/edituser', methods=["GET"])
def edituser():
    username = session.get('username')
    
    user_account = UserAccount.query.filter_by(username=username).first()
    user = User.query.filter_by(user_account_id=user_account.id).first()
        
    return render_template('edituser.html', user=user, user_account=user_account)

@app.route('/edituserrequest', methods=["GET","POST"])
def edituserrequest():
    username = session.get('username')
    
    # Retrieve user account data
    user_account = UserAccount.query.filter_by(username=username).first()
    print(user_account.username)
    # Check if user account exists
    if user_account:
        # Retrieve user data using user_account_id
        user = User.query.filter_by(user_account_id=user_account.id).first()
        print(user.id)
        
        # Check if user exists
        if user:
            if request.method == 'POST':
                # Handle form submission
                new_firstname = request.form.get("fname")
                new_lastname = request.form.get("lname")
                new_address = request.form.get("address")
                new_username = request.form.get("username")
                new_password = request.form.get("password")
                
                # Update user attributes
                user.fname = new_firstname
                user.lname = new_lastname
                user.address = new_address
                
                # Update user account attributes
                user_account.username = new_username
                user_account.password = new_password 

                db.session.commit()

                # Update session with new username if it has been changed
                session['username'] = new_username

                return redirect(url_for('index'))
            else:
                # Render edituser.html template with user data
                return render_template('edituser.html', user=user, user_account=user_account)
        else:
            # Handle case where user does not exist
            return render_template('error.html', message='User not found')
    else:
        # Handle case where user account does not exist
        return render_template('index.html')
        
    
    
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
    
    new_UserAccount = UserAccount(
        # email = request.form.get("email"),
        username = request.form.get("username"),
        password = request.form.get("password")
        
    )
    db.session.add(new_UserAccount)
    
    # new_UserAccount = session.get('id')
      
    db.session.add(new_UserAccount)
    db.session.commit() 
    
    new_User = User(
        fname = request.form.get("fname"),
        lname = request.form.get("lname"),
        address = request.form.get("address"),
        user_account_id=new_UserAccount.id
    )
    db.session.add(new_User)
    db.session.commit()
    
    return redirect(url_for('login'))

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)
