# coding: utf-8
import os


def getvar(key, default=None, template='OPENSHIFT_{key}'):
    """
    Get OPENSHIFT envvar
    """
    return os.environ.get(template.format(key=key), default)
