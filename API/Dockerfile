FROM python:3.14

WORKDIR /code

COPY dependencies.txt /code/

RUN pip install --no-cache-dir --upgrade -r dependencies.txt

COPY app/ ./app/

EXPOSE 8000