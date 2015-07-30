# coding: utf-8
import os
import sys
from .env import getvar


def envify(app=None, add_repo_to_path=True):
    """
    This will simply activate virtualenv on openshift ans returs the app

    in a wsgi.py or app.py in your openshift python web app
    - wsgi.py
    from shiftpy.wsgi_utils import envify
    from myproject import app
    # wsgi expects an object named 'application'
    application = envify(app)
    """
    if getvar('HOMEDIR'):
        if add_repo_to_path:
            sys.path.append(os.path.join(getvar('REPO_DIR')))

        sys.path.insert(0, os.path.dirname(__file__) or '.')

        virtenv = getvar('PYTHON_DIR') + '/virtenv/'
        virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
        exec_namespace = dict(__file__=virtualenv)

        try:
            if sys.version_info >= (3, 0):
                with open(virtualenv, 'rb') as f:
                    code = compile(f.read(), virtualenv, 'exec')
                    exec(code, exec_namespace)
            else:
                execfile(virtualenv, exec_namespace)  # noqa
        except IOError:
            pass

    return app
