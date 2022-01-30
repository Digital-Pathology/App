from flask import Blueprint, render_template, url_for, redirect
from DocumentUploadForm import DocumentUploadForm

backend = Blueprint('server', __name__)
home = Blueprint('home', __name__)


@backend.route('/server', methods=['GET', 'POST'])
def server():
    form = DocumentUploadForm()
    if form.validate_on_submit():
        print("successful upload")
        return '<h1>Upload Succesful </h1>'
    else:
        print("whoops")
    # FIXME: If the validation fails, then redirect to the home page.
    return render_template('home.html', form=form)

    # if request.method == 'GET':
    #     # if the status is 200, then send the data to the ML algorithm. Update the main page with a loading bar
    #     # to show the progress on classification.
    #     return '<p> GET </p>'
    # elif request.method == 'POST':
    #     return '<p> POST </p>'
    # else:
    #     abort(401)


@home.route('/')
@home.route('/home')
def home_page():
    form = DocumentUploadForm()
    return render_template("home.html", form=form)