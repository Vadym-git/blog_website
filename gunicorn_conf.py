import multiprocessing

command = '/home/vadym/websites/blog_website/.env/bin/gunicorn'
pythonpath = '/home/vadym/websites/blog_website/blog'
bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
user = 'vadym'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=blog.settings'