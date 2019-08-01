FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /src/
