from flask import Blueprint, render_template
from werkzeug.utils import secure_filename


#defining Blueprint for flask application
views = Blueprint('views',__name__)

## Defining route to home page
@views.route('/')
def home():
    return render_template("home.html")




