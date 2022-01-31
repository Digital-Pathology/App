from wtforms.fields import StringField, MultipleFileField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField


class DocumentUploadForm(FlaskForm):
    """DocumentUploadForm Object meant to create the form for submitting Whole Slide Image Data

    The form has 2 fields which are the EmailField, and the MultipleFileField. 
        The EmailField will have the pathologist set their email, so that when the image classification is done,
            they will be notified by email.
        The MultipleFileField will have the pathologist choose which of the Whole Slide Image files that they want to
            upload to the ML model.
    """
    # first_name = StringField('First Name', validators=[DataRequired()])
    # last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    file = MultipleFileField('Images', validators=[
        # FIXME :: FileRequired activates even though the POST request goes through perfectly
        FileRequired('FIX ME RIGHT NOW. THIS IS IN THE DocumentUploadForm.py'), 
        FileAllowed(['tiff', 'svs', 'jpg', 'jpeg', 'png'], 'Whole Slide Image Data Only!')
    ])


