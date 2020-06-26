# basic-backend-app

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
