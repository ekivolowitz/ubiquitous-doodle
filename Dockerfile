FROM python:3.7-stretch

COPY ./star_tides/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
WORKDIR /app
CMD python3 run.py