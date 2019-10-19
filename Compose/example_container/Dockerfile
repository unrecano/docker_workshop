FROM python:3
RUN mkdir /code
WORKDIR /code
COPY . .
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --verbose
EXPOSE 5000