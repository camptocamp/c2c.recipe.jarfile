#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'c2c.recipe.jarfile',
    version = '0.4.3',
    license = 'MIT License',

    author  = 'Frederic Junod',
    author_email = 'frederic.junod@camptocamp.com',
    url = 'https://github.com/fredj/c2c.recipe.jarfile',

    description = 'A buildout recipe to create or update jar archive file.',
    long_description = open('README.rst').read(),

    classifiers = [
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ],

    zip_safe = False, 
    install_requires = ['zc.buildout'],
    packages = find_packages(exclude=['ez_setup']),
    namespace_packages = ['c2c', 'c2c.recipe'],
    entry_points = {'zc.buildout' : ['default = c2c.recipe.jarfile.buildout:CreateUpdateJar']}
)
