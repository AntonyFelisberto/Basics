# Basics

## React

Creating React Project

    npm create vite@latest react-app -- --template react

Running project

     npm run dev

## Python

Create Python venv

    python -m venv venv

activate it

    cd venv/scripts
        activate
           OR
    .\venv\Scripts\activate
        
installing django with venv activated

    pip install django

installing rest framework manager

    pip install djangorestframework

create rest manager

    django-admin startproject django_rest_main .

apply changes made on django manager

    python manage.py migrate

create a django app (that will serve to integrate and create request)
    
    python manage.py startapp students
