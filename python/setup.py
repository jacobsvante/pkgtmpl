#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup
import codecs
import os
import sys


pkgname = '{{ package_name }}'
pkg = __import__(appname)
version = pkg.__version__


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:\ngit tag -a {} " \
          "-m 'version {}'\n  git push --tags".format(version, version))
    sys.exit()

setup(
    name=pkgname,
    version=version,
    description=pkg.__doc__.split('\n')[0],
    long_description=read(os.path.join(os.path.dirname(__file__),
                                       'README.md')),
    py_modules=[pkgname],
    packages=[],
    install_requires=[
        'sh>=1.0.8',
    ],
    author={{ full_name }},
    author_email={{ email }},
    url='https://github.com/{{ github_username }}/{{ package_name }}',
    license='BSD',
    platforms=['unix', 'macos'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
