from fabric.api import *


env.project_name = '{{cookiecutter.repo_name}}'


# ==========================================================================
#  Enviroments
# ==========================================================================

def vagrant():
    # get vagrant ssh setup
    vagrant_config = _get_vagrant_config()
    env.key_filename = vagrant_config['IdentityFile']
    env.hosts = ['%s:%s' % (vagrant_config['HostName'],
                            vagrant_config['Port'])]
    env.user = vagrant_config['User']


# ==========================================================================
#  Tasks
# ==========================================================================

def manage(cmd):
    local('python {project_name}/manage.py {cmd}'.format(
                            project_name=env.project_name, cmd=cmd))


def test():
    manage('test %(project_name)s' % env)


def shell():
    manage('shell')


def devserver(address='127.0.0.1:8000'):
    '''Start local development server'''
    manage('runserver %s' % address)


# ==========================================================================
#  Helpers
# ==========================================================================

def _get_vagrant_config():
    result = local('vagrant ssh-config', capture=True)
    conf = {}
    for line in iter(result.splitlines()):
        parts = line.split()
        conf[parts[0]] = ' '.join(parts[1:])
    return conf
