from flask import Flask, render_template
from os import environ
from re import DEBUG
from DataSharing import app
from DataSharing.views import views

if __name__ == '__main__':
    app.register_blueprint(views, url_prefix = '/home')

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, True)
