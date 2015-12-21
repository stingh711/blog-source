Title: How to deploy Django applications
Date: 2015-07-17 19:52:43
Tags: django, python, nginx, gunicorn
Category: python
Slug: deploy-django
Author: Sting
Summary: How to deploy Django applications.

We have a lot of small Django applications deployed on a single Ali cloud server. Following is my current setup. (I’m not a Django expert nor a linux expert, I just hope this post will help someone like me)

## Nginx as reverse proxy server.
Nginx’s performance is very well and much easier to configure than apache server.
## dj-static to server static and media files
Nginx can do the same thing, but need to change file permissions of static and media files. Dj-static is easier to use.
## Gunicorn as application server
Just use it following Django’s doc.
## Supervisord to start or stop the gunicorn server
I used to use tmux to start or stop the gunicorn server until I came cross this post: [https://hynek.me/articles/python-deployment-anti-patterns/][1]
Supervisor saved my life, because I run 5 Django applications and 5 java applications (run on jetty) on the server. I have 9 tmux sessions to  start or stop these applications… 

[1]:	https://hynek.me/articles/python-deployment-anti-patterns/
