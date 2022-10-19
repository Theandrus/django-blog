FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /myfirst

WORKDIR /myfirst

COPY requirements.txt /myfirst/

RUN pip install --upgrade pip && pip install -r requirements.txt

#ADD myfirst /myfirts/