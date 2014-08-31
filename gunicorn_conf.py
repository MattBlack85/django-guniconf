import getpass
import multiprocessing


bind = "unix:/var/run/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1 # This is the max suggested by gunicorn doc, tweak it on your needs
pidfile = "/home/var/run/gunicorn.pid"
threads = multiprocessing.cpu_count() * 4 # If you want threads you have to install trollius package
errorlog = "/var/log/gunierror.log"
loglevel = "debug"
accesslog = "/var/log/guniaccess.log"
daemon = True # If you're going to use supervisor or similar you should delete this line
user = getpass.getuser() # It gets the current user, change if you want it to run as another user
