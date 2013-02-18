#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


files = ['README.rst', 'CHANGELOG.rst', 'AUTHORS.rst']
long_description = '\n\n'.join(map(lambda fn: open(fn).read(), files))

setup(
    name="django-filefieldtools",
    version='1.0',
    description="Utilities upload files to model field",
    author="Pavel Koltyshev",
    author_email="pkoltyshev@gmail.com",
    url="https://github.com/pkolt/django-filefieldtools",
    long_description=long_description,
    license="BSD",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=1.4,<1.5",
        "trans>=1.5"
    ],
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
