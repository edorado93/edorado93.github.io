FROM ruby:2.5

WORKDIR /usr/src/app

# we put README.md as placeholder, because Docker cannot create empty container
COPY README.md ./

#create volume for later mounting of your local directory
VOLUME /usr/src/app