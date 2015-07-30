# shiftpy
Tools for running Python Apps on OpenShift Red Hat Cloud

[![Build Status](https://travis-ci.org/rochacbruno/shiftpy.svg?branch=master)](https://travis-ci.org/rochacbruno/shiftpy)
[![Code Health](https://landscape.io/github/rochacbruno/shiftpy/master/landscape.svg?style=flat)](https://landscape.io/github/rochacbruno/shiftpy/master)

<a target="_blank" href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=rochacbruno%40gmail%2ecom&amp;lc=BR&amp;item_name=ShiftPy&amp;no_note=0&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest"><img alt='Donate with Paypal' src='http://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif' /></a>


# installation

```pip install shiftpy```

# Available tools

- env.getvar - Get openshift env var
- env.listvars - Print all openshift env vars
- env.getallvars - Get all vars as a dict
- wsgi_utils.envify - Wrap wsgi app in Openshift Virtualenv
- **ADD YOURS, please contribute**

# getvar

```python
> from shiftpy.env import getvar
> print getvar('HOMEDIR')
'app-root/w543543543543543/home/'
```

# listvars


```python
> from shiftpy.env import listvars
> listvars()
OPENSHIFT_HOMEDIR = 'app-root/w543543543543543/home/'
OPENSHIFT_APP_NAME = 'yourappname'
...
```

# getallvars

```python
> from shiftpy.env import getallvars
> allvars = getallvars()
> print allvars
{'OPENSHIFT_FOO': 'BAR',
 'OPENSHIFT_HOMEDIR': '/tmp',
 'OPENSHIFT_PYTHON_DIR': '/tmp/python'}

```

# envify

This will wrap your wsgi app in virtualenv to OpenShift

```python
from shiftpy.wsgi_utils import envify
from myproject import app

# wsgi expects an object named 'application'
application = envify(app)

```

then your app will be available for wsgi_mod and virtualenv is activated
