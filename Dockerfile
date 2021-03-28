FROM python:3.7-stretch

# We copy just the requirements.txt first to leverage Docker cache
COPY ./star-tides/requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python3 run.py