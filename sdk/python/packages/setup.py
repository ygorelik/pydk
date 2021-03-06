#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------


"""Setup for YDK


"""
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

INSTALL_REQUIREMENTS = ['enum34==1.1.3',
                        'lxml>=3.4.4',
                        'ncclient>=0.4.7',
                        'ydk==0.5.5.post2']

NMSP_PKG_NAME = "$PACKAGE$"
NMSP_PKG_VERSION = "$VERSION$"
NMSP_PKG_DEPENDENCIES = ['$DEPENDENCY$']

if NMSP_PKG_DEPENDENCIES != "$DEPENDENCY$":
    INSTALL_REQUIREMENTS.extend(NMSP_PKG_DEPENDENCIES)

NMSP_PACKAGES = ['ydk', 'ydk.models']
YDK_PACKAGES = find_packages(exclude=['contrib', 'docs*', 'tests*',
                                      'ncclient', 'samples'])


DESCRIPTION = "$DESCRIPTION$"
LONG_DESCRIPTION = "$LONG_DESCRIPTION$"

setup(
    name=NMSP_PKG_NAME,
    version=NMSP_PKG_VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/CiscoDevNet/ydk-py',
    author='Cisco Systems',
    author_email='yang-dk@cisco.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C++'
    ],
    keywords='yang, C++11, python bindings',
    packages=YDK_PACKAGES,
    namespace_packages=NMSP_PACKAGES,
    install_requires=INSTALL_REQUIREMENTS
)
