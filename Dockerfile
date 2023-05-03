FROM python:3.7.0
MAINTAINER UHJ "umhj0807@khu.ac.kr"
COPY . /app
RUN apt-get update
RUN echo "this is a python web server container"
CMD ["python", "/app/webserver.py"]
EXPOSE 9000