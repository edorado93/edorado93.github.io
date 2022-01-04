FROM node:17

RUN apt-get -y update

RUN apt-get -y install git

RUN git clone https://github.com/dtesler/medium-to-markdown.git /medium-to-markdown

WORKDIR /medium-to-markdown

RUN cd /medium-to-markdown

RUN npm install

