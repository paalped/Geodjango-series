FROM python:3.7
ENV PYTHONUNBUFFERED 1
LABEL version="0.1a"
LABEL maintainer="Paal Pedersen"
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN apt-get install git
RUN git clone https://github.com/paalped/Geodjango-series.git
WORKDIR /Geodjango-series
RUN pip install -r requirements.txt
    
RUN	f=$(find / -name "manage.py") && \ 
	python3 $f makemigrations
RUN f=$(find / -name "manage.py") && \ 
	python3 $f migrate







