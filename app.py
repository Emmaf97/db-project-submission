from flask import Flask, render_template
# request, redirect, url_for, flash,session
# from flask_login import login_user, LoginManager, UserMixin, logout_user
# import json
# import os

app = Flask(__name__)
# Generate a random secret key of 32 bytes
# app.secret_key = os.environ.get('SECRET_KEY', 'dev')                                                          # Creating Secret key using standard practices to protect sensitive data.

# login_manager = LoginManager(app)                                                                             # Flask library - that manages login of the user on the server side. This is need to achieve login functionality with my approach.

# class User(UserMixin):                                                                                        # using the User class from the UserMixin library in order to monitor login of the user. Also good use of Object Oriented Programming.
#     def __init__(self, id, username, password,loggedin):
#         self.id = id
#         self.username = username
#         self.password = password
#         self.loggedin = loggedin
        

@app.route("/")
def index():
    # user_id = session.get('user_id')
    # loggedin = session.get('loggedin')
    # if user_id and loggedin:
    #     user = load_user(user_id)
        # return render_template('index.html', username=user.username, loggedin=user.loggedin)
    return render_template('index.html')

@app.route("/esports")
def esports():
    # user_id = session.get('user_id')
    # loggedin = session.get('loggedin')
    # if user_id and loggedin:
    #     print("schedule")
    #     user = load_user(user_id)
    #     return render_template('schedule.html', username=user.username, loggedin=user.loggedin)
    return render_template("esports.html")

@app.route("/news")
def news():
    # user_id = session.get('user_id')
    # loggedin = session.get('loggedin')
    # if user_id and loggedin:
    #     user = load_user(user_id)
    #     return render_template('trainers.html', username=user.username, loggedin=user.loggedin)
    return render_template("news.html")

@app.route("/store")
def store():
    # user_id = session.get('user_id')
    # loggedin = session.get('loggedin')
    # if user_id and loggedin:
    #     user = load_user(user_id)
    #     return render_template('videos.html', username=user.username, loggedin=user.loggedin)
    return render_template("store.html")

@app.route("/contact")
def contact():
    # user_id = session.get('user_id')
    # loggedin = session.get('loggedin')
    # if user_id and loggedin:
    #     user = load_user(user_id)
    #     return render_template('contact.html', username=user.username, loggedin=user.loggedin)              # Passng username and logged in status from server from server and displaying username if the user is logged in.
    return render_template("contact.html")

# def load_user(user_id):
#     json_file_path = os.path.join(app.static_folder, 'json', 'user.json')
#     with open(json_file_path, 'r') as file:
#         users = json.load(file)
#         for user in users["users"]:
#             if user["id"] == user_id:
#                 return User(user["id"], user["username"], user["password"],user["loggedin"])                # Creating a user object that uses flask login Manager UserMixin library. This helps to keep track of server side request such as login and user id.
#     return None

# login_manager.user_loader(load_user)

@app.route('/login')
def login():
    return render_template("login.html")
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template("login.html")
#     else:
#         username = request.form['username']
#         password = request.form['password']
    
#                                                                                                             # Using the authenticate function to check the username and password matched the data in the json file.
#         user = authenticate_user(username, password)
    
#         if user:
#             login_user(user)                                                                                # Using flasks login library to create and monitor user session.
#             session['user_id'] = user.id                                                                    # Store user ID in session(server side)
#             session['loggedin'] = user.loggedin                                                             # Store loggedin in session(server side)                                                                                            
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password.', 'error')                                                 # using flash libray to display messages to the user
#             return redirect(url_for('login'))

    

# def authenticate_user(username, password):
#     json_file_path = os.path.join(app.static_folder, 'json', 'user.json')                                   # Using for loop to go through a dictionary with a dictionary of users and then comparing the data to see if it matches and returning it to a user object.
#     with open(json_file_path, 'r') as file:
#         users_list = json.load(file)
#         for users_list in users_list.values():
#             for users in users_list:
#                 if users["username"] == username and users["password"] == password:
#                     users["loggedin"] = True
#                     return (User(users["id"], users["username"], users["password"] ,users["loggedin"]))         
#     return None
    

# @app.route('/logout', methods=['GET','POST'])
#                                                                                                             # had to remove the @login_required it was causing and error. could not figure out how to use it with the project setup for json.
# def logout():
#     if request.method == "GET":
#         logout_user()
#         session.clear()
#         return redirect(url_for('login'))

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     return render_template("signup.html")
@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)
