FROM python:3.9

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python -m flask run --host=0.0.0.0