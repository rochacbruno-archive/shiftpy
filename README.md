# shiftpy
Tools for running Python Apps on OpenShift Red Hat Cloud

# install

```pip install shiftpy```

# Tools

- env.getvar - Get openshift env var
- env.listvars - List all openshift env vars
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

# envify

This will wrap your wsgi app in virtualenv to OpenShift

```python
from shiftpy.wsgi_utils import envify
from myproject import app

# wsgi expects an object named 'application'
application = envify(app)

```

then your app will be available for wsgi_mod and virtualenv is activated