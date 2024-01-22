from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json



#defining this file as the 'blueprint' of our app, which means it will have a bunch of routes in it.
views = Blueprint('views',__name__)
@views.route('/')
@login_required
def home():
    return render_template("home.html") #calls the stated file to be displayed
