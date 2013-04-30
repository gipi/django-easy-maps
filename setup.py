#!/usr/bin/env python
from setuptools import setup
import os

from easy_maps import version

def dump_content(filename):
    "Dumps contents of a file relatively to the root directory"
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name = 'django-easy-maps',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://bitbucket.org/kmike/django-easy-maps/',

    description = 'This app makes it easy to display a map for a given address.',
    long_description = dump_content('README.rst') + '\n\n' + dump_content('CHANGES.rst'),
    license = 'MIT license',
    install_requires = [
        'django>=1.3',
        'geopy>=0.95',
    ],

    packages = [
        'easy_maps',
        'easy_maps.templatetags',
        'easy_maps.migrations'
    ],
    package_data = {
        'easy_maps': [
            'templates/easy_maps/*'
        ]
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
