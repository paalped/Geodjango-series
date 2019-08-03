# Geodjango Series Docker-Compose

This is a geodjango project is a fork from https://github.com/wanjohikibui/Geodjango-series

### Set Up
To set up the project, follow the steps;
make sure docker is installed and using linux containers.
navigate to the Docker folder in your terminal of choice or simply use commandline in windows.
to be sure db is  set up first run:
```
docker-compose up -d db
```
and then run:
```
docker-compose up -d web
```
### Develop on this repository
Simply click clone this repository into your own github account.
Use github desktop to create a local repository. 
Edit the Dockerfile to point to your github:
```
RUN git clone https://github.com/YOUR_USERNAME/Geodjango-series.git
```
Then you can do:
```
1. docker-compose up -d db

2. docker-compose up -d web
```

Just leave me a note if there is some issues.