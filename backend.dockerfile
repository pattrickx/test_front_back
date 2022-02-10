FROM python:3.8

ARG version=1.0.0-SNAPSHOT

COPY ./backend /home/backend

RUN apt-get update -y
RUN apt-get install -y libaio1


RUN yes | pip3 install Flask==2.0.1
RUN yes | pip3 install flask-cors==3.0.10
RUN yes | pip3 install requests==2.26.0
RUN yes | pip3 install gunicorn==20.1.0
RUN yes | pip3 install PyJWT==1.7.1
RUN yes | pip3 install flask_session

WORKDIR /home/backend

CMD gunicorn -w 4 "app:create_app(testing=False)" -b :5000 --reload --timeout 240 --log-level debug


