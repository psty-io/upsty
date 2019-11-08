#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='upsty',
    version='1.0',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='Command line tool for up.psty.io',
    long_description="""Command line tool for up.psty.io""",
    long_description_content_type='text/markdown',
    url='https://github.com/psty-io/upsty',
    packages=['upsty'],
    install_requires=[
        'requests'
    ],
    project_urls={
        'Wiki': 'https://github.com/psty-io/upsty/wiki',
        'Discord Server': 'https://discord.gg/HphdfxU'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'upsty = upsty.__main__:main',
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
