#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name             = 'opoona',
    version          = '0.1.0',
    description      = 'Opoona, the thicket opener.',
    license          = 'MIT',
    author           = 'Pine, Mihyaeru',
    author_email     = 'pinemz@gmail.com, mihyaeru@gmail.com',
    url              = 'http://github.com/pine/opoona',
    keywords         = 'opoona git issue github',
    packages         = ['opoona', 'opoona.tickets'],
    entry_points     = {'console_scripts': ['opoona = opoona:main']},
    install_requires = [
        'docopt >= 0.6.2',
        'github3.py >= 0.9.6',
        'PyYAML >= 3.12',
        'requests >= 2.12.4',
        'six >= 1.10.0',
    ],
)

