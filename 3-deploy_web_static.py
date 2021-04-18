#!/usr/bin/python3
"""Fabfile to create and distribute a new archive to both web server"""


from fabric.api import local, run, env, put
import time
import os


env.user = 'ubuntu'
env.hosts = ['35.190.130.61', '34.75.80.235']


def do_pack():
    """creates .tgz archive"""
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timestr))
        path = ("versions/web_static_{}.tgz".format(timestr))
        return (path)
    except:
        return None


def do_deploy(archive_path):
    """deploy archive"""

    if not archive_path:
        return(False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return(True)
    except BaseException:
        return(False)


def deploy():
    """ creates and distributes an archive to web server"""

    try:
        path = do_pack()
    except BaseException:
        return(False)
    do_deploy(path)
