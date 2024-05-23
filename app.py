from flask import Flask, render_template


app = Flask(__name__)

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

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, port=8080)
