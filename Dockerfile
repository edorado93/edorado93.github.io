FROM ruby:2.5

RUN bundle config --global frozen 1

WORKDIR /usr/src/app

# prepare to install ruby packages into container
COPY Gemfile Gemfile.lock minimal-mistakes-jekyll.gemspec ./

RUN bundle install

VOLUME /usr/src/app

EXPOSE 4000

CMD ["jekyll", "serve"]