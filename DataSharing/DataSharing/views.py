"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Blueprint, render_template
from DataSharing import app
from Models.User import User
from MongoDbManager import MongoDbManager


views = Blueprint( "views", __name__)

@app.route('/navigate', methods=['POST'])
def navigate():
    destination = request.form['destination']
    if destination == 'about':
        return redirect('/about')
    elif destination == 'contact':
        return redirect('/contact')
    else:
        # Handle invalid destination
        return redirect('/')

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='DataSharing', # Argument that sent to the page title.
        year=datetime.now().year,
    )

#@views.route('register')
@app.route('/register', methods = ['GET', 'POST'])
def registerpage():
    return render_template('register.html', title = 'Register')

@app.route('/registerprocess', methods = ['GET'])
def register_process(request):
    if request.method == 'Get':
        username = request.form["username"]
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        
        new_user = User(username, f_name, l_name, email, password)
        db_Manager = MongoDbManager("DataSharing", "Users")
        db_Manager.insert(new_user)
        return render_template('welcome.html')

@views.route('/')
@views.route('welcome')
@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template(
        'welcome.html',
        title='DataSharing' # Argument that sent to the page title.
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
