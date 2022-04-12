# DP-WebApp
[![Tests Status](./test-badge.svg)](./reports/junit/report.html)

* This is supposed to be setup in a Python virtual environment, so you can do that by:

  * Typing "python -m venv ." when you are inside this directory. 
  * And then do "source Scripts/activate" if in bash, or ".\Scripts\activate" if in Powershell. 
  * And then to get the dependencies, you should be able to just do "pip install -r requirements.txt"


To deactivate the virtual environemnt, type "deactivate" in the command line.



To get the flask app up and running:
  * In Bash, do "export FLASK_APP=app.py" and "export FLASN_ENV=development", and then "flask run". 
    * Or run the runBeforeStart.sh shell command in the bash command line
  * In Powershell, do '$env:FLASK_ENV = "app.py"' '$env:FLASK_ENV = "development"'
    * Or run the runBeforeStart.ps1 powershell command in the powershell command line



* Current TODOs:
  * CSS for the Home page
  * CSS for the Server page
  * CSS for the Form in general
  * Backend creation for ML support
  * Form validation and testing 
  * UNKNOWN :: TESTING REQUIRED
