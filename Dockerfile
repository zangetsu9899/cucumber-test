FROM python:3.11 as base

WORKDIR /opt/restapi_testfwk
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /opt/restapi_testfwk
