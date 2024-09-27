# Build and push service1 Docker image
docker build -t <your-docker-username>/service1:latest ./service1
docker push <your-docker-username>/service1:latest

# Repeat for service2 and service3
docker build -t <your-docker-username>/service2:latest ./service2
docker push <your-docker-username>/service2:latest

docker build -t <your-docker-username>/service3:latest ./service3
docker push <your-docker-username>/service3:latest
