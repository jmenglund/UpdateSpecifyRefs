#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname
from io import open


setup(
    name='UpdateSpecifyRefs',
    version='0.1.0',
    description=(
        'Command-line utility for updating record '
        'references in a Specify database.'),
    long_description=open(
        join(dirname(__file__), 'README.rst'), encoding='utf-8').read(),
    py_modules=['update_specify_refs'],
    install_requires=['pymysql', 'CountRecordRefs'],
    entry_points={
        'console_scripts': [
            'UpdateSpecifyRefs.py = update_specify_refs:main']},
    author='Markus Englund',
    author_email='jan.markus.englund@gmail.com',
    url='https://github.com/jmenglund/UpdateSpecifyRefs',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database',
        'Topic :: Utilities',
    ],
    keywords=['MySQL', 'Specify'])
