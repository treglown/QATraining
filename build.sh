docker build -t jenkinsimage .
docker run -d -p 80:5500 --name Container jenkinsimage