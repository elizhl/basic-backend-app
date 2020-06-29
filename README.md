# basic-backend-app

<img width="814" alt="Screen Shot 2020-06-26 at 11 39 24" src="https://user-images.githubusercontent.com/51725996/85880647-f9fdd100-b7a1-11ea-9d09-ac6a01f44c7d.png">

Clone the project

Create a virtualenv then run

    pip install requirements.txt
    flask run
    

If you prrefer you can use the docker image

    docker pull elizhl/basic-backend-app
    docker build -t basic-backend-app:latest .
    docker run -p 5000:5000 basic-backend-app
    
Go to http://0.0.0.0:5000

Done!