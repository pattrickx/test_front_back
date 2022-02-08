FROM node:lts-alpine

RUN npm install -g http-server
COPY ./frontend /app
WORKDIR /app

RUN npm install
RUN npm run build

CMD [ "http-server", "build" ]