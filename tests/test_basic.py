# coding: utf-8
import os
from shiftpy.env import getvar, listvars, getallvars
from shiftpy.wsgi_utils import envify


def test_env_getvar():
    assert os.environ['OPENSHIFT_FOO'] == getvar('FOO')


def test_wsgi_envify():
    app = envify('foobar')
    assert app == 'foobar'
    assert getvar('HOMEDIR') == '/tmp'
    assert getvar('PYTHON_DIR') == '/tmp/python'


def test_env_listvars():
    listvars()


def test_env_getallvars():
    allvars = getallvars()
    assert allvars['OPENSHIFT_FOO'] == 'BAR'
    assert allvars['OPENSHIFT_HOMEDIR'] == '/tmp'
    assert allvars['OPENSHIFT_PYTHON_DIR'] == '/tmp/python'
