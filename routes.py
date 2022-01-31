from flask import Blueprint, render_template, url_for, redirect, request
from DocumentUploadForm import DocumentUploadForm
from pprint import pprint

backend = Blueprint('server', __name__)
home = Blueprint('home', __name__)

ALLOWED_EXTENSIONS = {'tiff', 'svs','jpg', 'jpeg','png','JPG','JPEG','PNG'}

def allowed_file(File):
    return '.' in File.filename and File.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@backend.route('/server', methods=['GET', 'POST'])
def server():
    form = DocumentUploadForm()
    files = request.files.getlist('file')
    files = list(filter(allowed_file, files))
    if request.method == 'POST':
        if files:
            return render_template('home.html', form=form, loadingbar=True)

        # return redirect(url_for('home.home_page'))
    # if the status is 200, then send the data to the ML algorithm. 
    # Update the main page with a loading bar
    # to show the progress on classification.
    elif request.method == 'GET':
        return '<h1> GET -- Unimplemented </h1>'
    else:
        # FIXME: If the validation fails, then redirect to the home page.
        return render_template('home.html', form=form, loadingbar=False)


@home.route('/')
@home.route('/home')
def home_page():
    form = DocumentUploadForm()
    return render_template("home.html", form=form, loadingbar=False)