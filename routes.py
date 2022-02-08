from flask import Blueprint, render_template, url_for, redirect, request
import asyncio
from DocumentUploadForm import DocumentUploadForm
from pprint import pprint
from time import sleep

backend = Blueprint('server', __name__)
home = Blueprint('home', __name__)

ALLOWED_EXTENSIONS = {'tiff', 'svs', 'jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'}

def allowed_file(File):
    return '.' in File.filename and File.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def sendTheModel(images):
    """Send the images to the model in the backend, and await for the response from the
       server.
    """
    await asyncio.sleep(2)
    
    return '<h1>this is the model</h1>'


@backend.route('/server', methods=['GET', 'POST'])
async def server():
    form = DocumentUploadForm()
    files = list(filter(allowed_file, request.files.getlist('file')))
    if request.method == 'POST':
        if files:
            modelResponse = await sendTheModel(files)
            return modelResponse
            # return render_template('home.html', form=form, loadingbar=True)   
    return redirect(url_for('home.home_page'))


@home.route('/')
@home.route('/home')
def home_page():
    form = DocumentUploadForm()
    return render_template("home.html", form=form, loadingbar=False)