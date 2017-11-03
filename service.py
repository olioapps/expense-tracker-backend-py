# hosts flask, takes in an api and delegates routes to actions in the api

from flask import Flask
app = Flask(__name__)

class Service:

    @app.route('/')
    def index():
        return "Hello World!"

    @app.route('/api/v2/mydata')
    def hello():
        return "Yo World!"

    @app.route("/user/<username>")
    def show_user_profile(username):
        return 'Username: %s' % username

    @app.route("/clients/")
    def clients(slef):
        return 'The Clients Summary Page'

    def run(self):
        app.run(host="0.0.0.0")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")