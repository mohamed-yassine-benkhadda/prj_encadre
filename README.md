```
git pull https://github.com/mohamed-yassine-benkhadda/prj_encadre.git
```

```
cd prj_enc
```

#### 1. place html code in ``` templates ``` folder
#### 2. place css js and img files in ``` static ``` folder
#### 3. add ```{% load static%}``` in the ```<head></head>```

```
git add .
```

```
git commit -m "your message"
```

```
git push
```

#### Create a blank database in mysql & In settings modify the database informations

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'prj_enc',
        'USER' : 'root',
        'PASSWORD' : '',
        'Host' : 'localhost',
        'PORT' : '3306',
    }
}
```

#### after every modification in models.py or settings.py issue the following commands in cmd (make sure to be in prj_enc folder)

```
python manage.py makemigrations
python manage.py migrate
```

#### Run the server locally 

```
python manage.py runserver
```
