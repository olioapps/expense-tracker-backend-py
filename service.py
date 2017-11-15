# hosts flask, takes in an api and delegates routes to actions in the api

from flask import Flask
app = Flask(__name__)

class Service:

    def __init__(self):
        print("constructed")

    @app.route('/')
    def index(self):
        return "Hello World!"

    @app.route('/api/v2/mydata')
    def hello(self):
        return "Yo World!"


    ### User endpoints

    @app.route("/user/create<User>")
    def create_user(self, User):
        return 'create new user: %s' % User

    # @app.route("/user/delete<userID>")
    # def delete_user(self, userID):
    #     return 'delete user: %s' % userID

    @app.route("/user/<username>")
    def show_user_profile(self, username):
        '''return user profile for username '''
        return 'Username: %s' % username

    @app.route("/get_users/")
    def get_users(self):
        '''return user info for all users '''

    @app.route("/user/edit<User>")
    def edit_user(self, User):
        return 'edit user: %s' % User


    ### Login endpoints

    @app.route("/login/")
    def login(self):
        return 'The Login Page'

    @app.route("/login/submit/<username><pin>")
    def submit_login(self, username, pin):
        return 'edit user: %s %s' % username, pin


    ### R U N

    def run(self):
        app.run(host="0.0.0.0")
