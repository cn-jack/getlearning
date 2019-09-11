import multiprocessing
import os
import os.path

LOG_DIR = "../log"

os.makedirs(LOG_DIR, exist_ok=True)

daemon = True
debug = True
loglevel = 'debug'

pidfile = os.path.join(LOG_DIR, "gunicorn.pid")
accesslog = os.path.join(LOG_DIR, "access.log")
errorlog = os.path.join(LOG_DIR, "error.log")

bind = "127.0.0.1:8000"
backlog = 2048
workers = multiprocessing.cpu_count()
worker_connections = 1000
proc_name = 'www.getlearning.cn'
x_forwarded_for_header = 'X-FORWARDED-FOR'
