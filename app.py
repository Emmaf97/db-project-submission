from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy import text										
# from models import db, User, Email     
from models import db, User, UserAccount, Products , UserComments  


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)												

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/esports")
def esports():
    return render_template("esports.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/login')
def login():
    return render_template("login.html")

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
    # new_user = User(fname='John', lname='Doe', address='123 Main St')
    # db.session.add(new_user)
    db.session.add(new_User)
    
    new_UserAccount = UserAccount(
        # email = request.form.get("email"),
        username = request.form.get("username"),
        password = request.form.get("password")
        
    )
    # new_user_account = UserAccount(username='johndoe', password='hashed_password')
    # db.session.add(new_user_account)
    db.session.add(new_UserAccount)
    db.session.commit()
    
    return redirect(url_for('login'))

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)
