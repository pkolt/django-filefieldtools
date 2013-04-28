#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from distutils.core import setup


base_dir = os.path.dirname(__file__)
files = ['README.rst', 'CHANGELOG.rst', 'AUTHORS.rst']
long_description = '\n\n'.join(map(lambda fn: open(os.path.join(base_dir, fn)).read(), files))


setup(
    name="django-filefieldtools",
    version='1.0.3',
    description="Utilities upload files to model field",
    author="Pavel Koltyshev",
    author_email="pkoltyshev@gmail.com",
    url="https://github.com/pkolt/django-filefieldtools",
    long_description=long_description,
    license="BSD",
    packages=['filefieldtools'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Languagr :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
