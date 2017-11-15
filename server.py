#!/usr/bin/python

from service import *

class Server:


    ''' Pulls in the api and service, binds them together and calls run on the service... '''

    def main():
        myService = Service()

        print("Open a browser to http://localhost:5000/")

        myService.run()

    if __name__ == '__main__':
        main()
