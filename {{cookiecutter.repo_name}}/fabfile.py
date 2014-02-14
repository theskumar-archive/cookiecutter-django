from fabric.api import *

env.project_name = '{{cookiecutter.project_name}}'

# ==========================================================================
#  Enviroments
# ==========================================================================

def staging():
    env.remote = 'staging'
    env.branch = 'staging'

def dev():
    env.remote = 'dev'
    env.branch = 'dev'


# ==========================================================================
#  Tasks
# ==========================================================================

def setup():
    local('pip install -r requirements/local.txt')
    manage('syncdb')
    manage('migrate')
    manage('createsuperuser')


def manage(cmd):
    local('python {project_name}/manage.py {cmd}'.format(
                            project_name=env.project_name, cmd=cmd))

def test():
    manage('test %(project_name)s' % env)


def shell():
    manage('shell')


def serve(address='127.0.0.1:8000'):
    '''Start local development server'''
    manage('runserver %s' % address)


def deploy():
    test()
    local('git push origin %(branch)s' % env)
    local('git push %(remote)s %(branch)s:master' % env)


def setup_mac():
    local('brew install libmemcached')
