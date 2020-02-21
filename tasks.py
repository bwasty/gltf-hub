"""
Examples/hints for invoke:
```
$ inv --list # short: -l
$ inv --help start # short: -h
$ inv up -d
```
"""

from invoke import task

# NOTE: see invoke.yml for global config

@task
def up(c, detach=False):
    """ Start the backend with docker-compose (add -d for detached mode) """
    c.run(f'docker-compose up --build {"-d" if detach else "" }')

@task
def down(c, volumes=False):
    """ Stop backend (if running in detached mode). Add -v to remove all columes, including DB data. """
    c.run(f'docker-compose down { "-v" if volumes else "" }')

@task
def init_db(c, delete_first=False):
    """ Initialises a dev database, optionally first removing it (-d)"""
    if delete_first:
        c.run('docker-compose stop db && '
              'docker-compose rm -f db && '
              'docker volume rm gltf-hub_postgres-data',
              warn=True)
        c.run('docker-compose up -d db')
    c.run(f'docker-compose exec app python manage.py migrate && '
          f'docker-compose exec app python manage.py loaddata users.yaml')

@task(aliases=['l'])
def logs(c):
    """ Shortcut for docker-compose logs -f """
    c.run(f'docker-compose logs -f')

@task(aliases=['s'])
def shell(c, command='bash'):
    """ shortcut for docker-compose exec api bash  """
    c.run(f'docker-compose exec api { command }')
