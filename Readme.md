## Website: https://wwww.meetaditya.space/

## Use docker container 

#### Pull the image
```
docker pull adityadoker/portfolio:version2
```
#### Run the container on 8000 port
```
docker run -it --rm -p 8000:8000 aditya/website
```

## OR

## Build 
```
docker build -t portfolio-docker . 
```

## OR setup the enviornment

### Create virtualenv
```
virtualenv env
cd env/scripts
activate
cd ../..
```

### Install the dependencies
```
pip install -r requirements.txt
```

### Run the server
```
python manage.py runserver 
```