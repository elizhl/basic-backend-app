docker rm -f elizhl/basic-backend-app

docker rmi elizhl/basic-backend-app

docker image prune -f

docker volume prune -f

docker build -t elizhl/basic-backend-app .

docker tag elizhl/basic-backend-app elizhl/basic-backend-app

docker push elizhl/basic-backend-app