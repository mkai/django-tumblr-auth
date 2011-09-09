#! -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-tumblr-auth',
    version=__import__('tumblr_auth').__version__,
    author='Gökmen Görgen',
    author_email='gokmen@alageek.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/alageek/django-tumblr-auth',
    license='BSD',
    description=u' '.join(__import__('tumblr_auth').__doc__.splitlines()).strip(),
    install_requires=['django-social-auth>=0.3.3', 'oauth>=1.0.1'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
)
