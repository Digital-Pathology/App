
from threading import Thread

from flask import Blueprint, render_template, request
from DocumentUploadForm import DocumentUploadForm

from .diagnosis import DiagnosisRunner
from .file_handling import save_file_from_request
from . import config

backend = Blueprint('server', __name__)
home = Blueprint('home', __name__)


@home.route('/')
@home.route('/home')
def home_page():
    """ renders the homepage """
    form = DocumentUploadForm()
    return render_template("home.html", form=form, loadingbar=False)


ALLOWED_EXTENSIONS = {'tiff', 'svs', 'jpg', 'tif',
                      'jpeg', 'JPG', 'JPEG'}


def allowed_file(File):
    """ checks if the file is allowed based on extension """
    return '.' in File.filename and File.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


diagnosis_runners = []


@backend.route('/server', methods=['GET', 'POST'])
def server():
    """ starting the diagnosis thread """
    # form = DocumentUploadForm()
    print(request)
    file = list(filter(allowed_file, request.files.getlist('file')))
    print(f"{file = }")
    if request.method == 'POST':
        if file:
            print(file)
            print("Creating the threads and kicking them off")
            f = save_file_from_request(file[0])
            print(f)
            diagnosis_runner = DiagnosisRunner(config.DIAGNOSTIC_MODEL)
            diagnosis_thread = Thread(
                target=diagnosis_runner.do_diagnosis, args=(f,))
            diagnosis_thread.start()
            diagnosis_runners.append(diagnosis_runner)
    return render_template("diagnosis.html")


@backend.get('/modelStatus')
def model_status():
    """ updates the user on diagnostic progress """
    if len(diagnosis_runners) == 0:
        return {"status": "not_started"}
    return {i: diagnosis_runners[i].read_status() for i in range(len(diagnosis_runners))}
