# hosts flask, takes in an api and delegates routes to actions in the api

from flask import Flask
app = Flask(__name__)

class Service:

    def __init__(self):
        print("constructed")

    @app.route('/')
    def index():
        return "Hello World!"

    @app.route('/api/v2/mydata')
    def hello():
        return "Yo World!"

    @app.route("/clients/")
    def clients(self):
        return 'The Clients Summary Page'

    # user endpoints
    @app.route("/user/<username>")
    def show_user_profile(username):
        return 'Username: %s' % username

    @app.route("/getUser/")
    def get_user():
        '''return username of all users '''



    def run(self):
        app.run(host="0.0.0.0")
