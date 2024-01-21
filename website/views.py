from flask import Blueprint, render_template
#defining this file as the 'blueprint' of our app, which means it will have a bunch of routes in it.
views = Blueprint('views',__name__)
@views.route('/')
def home():
    return render_template("home.html") #calls the stated file to be displayed
