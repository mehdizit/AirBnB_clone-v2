#!/usr/bin/python3
"""Fabric script that generates a .tgz"""

from fabric.api import local
import time


def do_pack():
    """creates .tgz archive"""
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except:
        return None
