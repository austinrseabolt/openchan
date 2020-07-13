# openchan
A modern, open source imageboard inspired by the Japanese website 2channel, built entirely in Django. Currently in development, it is planned to be easily customizable and deployable, even for those with a minimal understanding of Python.

## Features:
- Configure your settings via the built in Django Admin menu.
- Easy board deployment
- Add mod warnings to posts
- Easily extendable 

## Installation:
After setting up your web server environment with your WSGI server of choice, perform these simple steps to get your openchan instance configured. I've included an sqlite database that has already had migrations performed, but if you'd like to use another database engine simply apply the migrations using manage.py.

- Log in to the Django Admin interface. Default credentials are Username="Admin" Password="openchan". 
- Change the password for Admin
- Under the Mainapp settings, click openchan instance > Site Settings to change the name of your site.
- Add boards and start posting!
