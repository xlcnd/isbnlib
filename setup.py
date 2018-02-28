# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# isbnlib -- tools for extracting, cleaning and transforming ISBNs
# Copyright (C) 2014-2018 Alexandre Lima Conde

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup
from isbnlib import __version__


setup(
    name='isbnlib',
    version=__version__,
    author='xlcnd',
    author_email='xlcnd@outlook.com',
    url='https://github.com/xlcnd/isbnlib',
    download_url='https://github.com/xlcnd/isbnlib/archive/v3.8.4.zip',
    packages=['isbnlib',
              'isbnlib/dev',
              'isbnlib/_data',
              'isbnlib/test',
              ],
    license='LGPL v3',
    description='Extract, clean, transform, hyphenate and metadata for ISBNs (International Standard Book Number).',
    long_description=open('README.rst').read(),
    keywords='ISBN metadata World_Catalogue Google_Books Open_Library BibTeX EndNote RefWorks MSWord opf BibJSON',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
