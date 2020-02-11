from fabric.api import env, cd, local, run

env.hosts = ['alu6616.me']


def deploy():
    local('git push')
    with cd('~/webapps/vmweb'):
      run('git pull')
    run('supervisorctl restart vmweb')
