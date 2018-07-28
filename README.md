# BIOsferra [![Build Status](https://travis-ci.org/temi4000/Biosferra.svg?branch=master)](https://travis-ci.org/temi4000/Biosferra)

Biosferra is a web platform that helps small producers of fruits and vegetable to sell their products.

![trol](https://user-images.githubusercontent.com/19783030/42413819-15ce0c40-8231-11e8-9943-afefd2565b45.png)

There are 2 types of users:
1. Sellers
2. Buyers

# How does it works?

Every single user has to complete a formular with personal informations. The difference between these user is that we need from sellers 2 documents that says they can sell their products. An admin will approve or not the register formular for sellers based on their documents. Also, their posts will be verified.

Here, buyers can buy fruits or vegetables from sellers and rating/reviewing their profile/posts. Users don't have to worry about transportation because biosferra's company will get rid of that.

# DATABASE DIAGRAM
![database_diagram](https://user-images.githubusercontent.com/19783030/43359105-b1aa75f2-92a5-11e8-9f5e-a96f402ebd92.png)


# Deploy

```sh
$  pip install -r requirements.txt 
```

```sh
$  cd info
```

 ```sh
$  python manage.py makemigrations
```

 ```sh
$  python manage.py migrate
```

 ```sh
$  python manage.py runserver 
```

## Technologies used
* Html
* Css
* JavaScript
* Python
* Django
* Bootstrap 4
* MySQL
* Material Design
* Materialize

## Packages used
* django
* django-widget-tweaks
* django-recaptcha
* gunicorn
* django-phonenumber-field
* Pillow




