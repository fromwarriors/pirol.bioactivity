# -*- coding: utf-8 -*-
# (c) 2013 Maciej Szymkiewicz
# Licensed under the MIT license: http://opensource.org/licenses/MIT
from setuptools import setup, find_packages

version = None
requires = [
]

setup(
    name='pirol.bioactivity',
    version=version,
    description='',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/zero323/pirol.bioactivity',
    license='MIT',
    author='Maciej Szymkiewicz',
    author_email='matthew.szymkiewicz@gmail.com',
    zip_safe=False,
    long_description=open('README.md').read(),
    include_package_data=True,
    namespace_packages=['pirol'],
    install_requires=requires,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite='pirol.bioactivity.tests',
)
