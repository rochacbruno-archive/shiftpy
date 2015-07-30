# coding: utf-8
import os
import pprint


def getvar(key, default=None, template='OPENSHIFT_{key}'):
    """
    Get OPENSHIFT envvar
    """
    return os.environ.get(template.format(key=key), default)


def getallvars(startswith='OPENSHIFT_'):
    return {
        key: value for key, value in os.environ.items()
        if key.startswith(startswith)
    }


def listvars(startswith='OPENSHIFT_'):
    pprint.pprint(getallvars(startswith))
