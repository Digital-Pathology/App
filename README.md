# DP-WebApp

## This WebApp must be run within the docker-image of Digital-Pathology.
There must be a .flaskenv file with the following lines:
- FLASK_APP=app.py
- FLASK_ENV=development

## Enter either of the following commands in the terminal of the WebApp directory:
* flask run
* python -m flask run

## Go to your browser and type [ http://localhost:5000 ](http::/localhost:5000)
![screen0](https://user-images.githubusercontent.com/69324309/168503317-61b9f8b9-ef3b-42d6-8e4b-3e2dbf5ee0c3.png)

## You should then see a webapp with the following screen. 
* Enter your details in the email field, add a tiff image, and choose the name of the model that you would like to use.
* The model name should located in the [models](models) subfolder.

![screen7](https://user-images.githubusercontent.com/69324309/168503802-0a5f0f13-2a81-4210-8abf-be5846d39303.png)

## Submit the image by pressing the Submit Images button
* Wait for the Image to be sent to the back end for processing ...

## Wait for the model to do its magic
![screen8](https://user-images.githubusercontent.com/69324309/168503995-340e5720-e903-445c-b6f9-cf700b34d44b.png)

## See the results of the model on your image!
