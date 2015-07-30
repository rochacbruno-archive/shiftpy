
# Fix for older setuptools
import re
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read('README.md')


# grep shiftpy/__init__.py since python 3.x cannot
# import it before using 2to3
file_text = read(fpath('shiftpy/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    name='shiftpy',
    version=grep('__version__'),
    url='https://github.com/rochacbruno/shiftpy/',
    license='MIT',
    author=grep('__author__'),
    author_email=grep('__email__'),
    description='Tools for Python Apps on OpenShift Red Hat Cloud',
    long_description=desc(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
