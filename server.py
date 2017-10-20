from flask import Flask
app = Flask(__name__)

@app.route('/api/v2/mydata')
def index():
    return "Hello World!"

@app.route("/user/<username>")
def show_user_profile(username):
    return 'Username: %s' % username

@app.route("/clients/")
def clients():
    return 'The Clients Summary Page'

if __name__ == "__main__":
    app.run(host="0.0.0.0")