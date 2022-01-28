from flask import Flask, render_template
from flask import request
import flask_bootstrap

app = Flask(__name__)


@app.route('/server', methods=['GET', 'POST'])
def server():
    if request.method == 'GET':
        # if the status is 200, then send the data to the ML algorithm. Update the main page with a loading bar
        # to show the progress on classification.
        return '<p> GET </p>'
    elif request.method == 'POST':
        return '<p> POST </p>'
    else:
        abort(401)


@app.route('/')
def home_page():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
