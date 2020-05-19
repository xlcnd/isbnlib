# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# isbnlib -- tools for extracting, cleaning and transforming ISBNs
# Copyright (C) 2014-2019 Alexandre Lima Conde
# SPDX-License-Identifier: LGPL-3.0-or-later

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

from datetime import datetime as dt
from setuptools import setup
from isbnlib import __version__

PROJECT_NAME = 'isbnlib'
PROJECT_PACKAGE_NAME = 'isbnlib'
PROJECT_LICENSE = 'LGPL v3'
PROJECT_LICENSE_URL = 'https://github.com/xlcnd/isbnlib/blob/dev/LICENSE-LGPL-3.0-only.txt'
PROJECT_AUTHOR = 'Alexandre Lima Conde'
PROJECT_COPYRIGHT = ' 2014-{}, {}'.format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://github.com/xlcnd/isbnlib'
PROJECT_EMAIL = 'xlcnd@outlook.com'
PROJECT_VERSION = __version__

PROJECT_GITHUB_USERNAME = 'xlcnd'
PROJECT_GITHUB_REPOSITORY = 'isbnlib'

GITHUB_PATH = '{}/{}'.format(PROJECT_GITHUB_USERNAME,
                             PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = 'https://github.com/{}'.format(GITHUB_PATH)

DOWNLOAD_URL = '{}/archive/{}.zip'.format(GITHUB_URL, 'v' + PROJECT_VERSION)
PROJECT_URLS = {
    'Bug Reports': '{}/issues'.format(GITHUB_URL),
    'Dev Docs': 'https://isbnlib.readthedocs.io/en/latest/devs.html',
    'Forum': 'https://stackoverflow.com/search?tab=newest&q=isbnlib',
    'License': PROJECT_LICENSE_URL,
}

PYPI_URL = 'https://pypi.org/project/{}/'.format(PROJECT_PACKAGE_NAME)
PYPI_CLASSIFIERS = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Text Processing :: General',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

PACKAGES = [
    'isbnlib',
    'isbnlib/dev',
    'isbnlib/_data',
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    license=PROJECT_LICENSE,
    description=
    'Extract, clean, transform, hyphenate and metadata for ISBNs (International Standard Book Number).',
    long_description=open('README.rst').read(),
    keywords=
    'ISBN metadata World_Catalogue Google_Books Wikipedia Open_Library BibTeX EndNote RefWorks MSWord opf BibJSON',
    classifiers=PYPI_CLASSIFIERS,
)
