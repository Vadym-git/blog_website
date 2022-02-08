#!/bin/bash
source /home/vadym/websites/blog_website/.env/bin/activate
source /home/vadym/websites/blog_website/.env/bin/postactivate
exec gunicorn  -c "/home/vadym/websites/blog_website/gunicorn_conf.py" blog.wsgi