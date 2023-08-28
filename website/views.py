from flask import Blueprint

#defining Blueprint for flask application

views = Blueprint('views',__name__)

## Defining route to home page
@views.route('/')
def home():
    return '<h1> HOME </h1>'


