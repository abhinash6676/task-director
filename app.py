from flask import Flask
app = Flask(__name__)
def opening():
    return "<p>This is a task managing app.<p>"