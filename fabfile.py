from fab_deploy import *
import fab_deploy.deploy
from fab_deploy import utils

def dev():
    #local("pip install -r reqs/all.txt")
    local("pip install -r reqs/dev.txt")
    local("python manage.py syncdb --noinput")
    local("python manage.py migrate --noinput")
    local("python manage.py loaddata fixtures/*")
    local("git init")
    local("git add .")
    local("git commit -m \"init\"")

def staging():
    env.hosts = ['gruzoved@u16586.netangels.ru']
    env.conf = dict(
        DB_PASSWORD = '3bazpomt',
        DB_ROOT_PASSWORD = 'hebun7lecig',
        DB_USER = 'gruzoved',
        VCS = 'git',
        LOCAL_CONFIG = 'local_settings.py',
        REMOTE_CONFIG_TEMPLATE = 'local_settings.server.py',
        SERVER_ADMIN = 'support@zavode.ru',
        APACHE_PORT = 8085,
    )
    update_env()

#cms_project()
