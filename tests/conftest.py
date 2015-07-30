# coding: utf-8
import os


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    os.environ['OPENSHIFT_FOO'] = 'BAR'
    os.environ['OPENSHIFT_HOMEDIR'] = '/tmp'
    os.environ['OPENSHIFT_PYTHON_DIR'] = '/tmp/python'
