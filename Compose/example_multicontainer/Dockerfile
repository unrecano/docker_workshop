FROM python:3
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --verbose
EXPOSE 3000
