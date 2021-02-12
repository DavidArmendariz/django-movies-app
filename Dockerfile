FROM python:3.9.1-slim-buster

WORKDIR /usr/src/app

# python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# pip
RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry export -o requirements.txt
RUN pip install -r requirements.txt

COPY ./src .

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]