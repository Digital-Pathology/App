
import os

from werkzeug.utils import secure_filename

from . import config

def save_file_from_request(file_storage_object):
    filename = secure_filename(file_storage_object.filename)
    filepath = os.path.join(config.UPLOADS_DIR, filename)
    file_storage_object.save(filepath)
    return filepath
