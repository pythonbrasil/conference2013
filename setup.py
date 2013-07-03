# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '1.0'
long_description = open("README.rst").read() + "\n" + \
    open(os.path.join("docs", "INSTALL.rst")).read() + "\n" + \
    open(os.path.join("docs", "CREDITS.rst")).read() + "\n" + \
    open(os.path.join("docs", "HISTORY.rst")).read()

setup(
    name='conference2013',
    version=version,
    description="Plone Conference and Python Brasil 2013 site",
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='ploneconf pythonbrasil conference',
    author='PloneGov.BR',
    author_email='gov@plone.org.br',
    url='https://github.com/plonegovbr/conference2013',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
#    namespace_packages=['conference2013'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'apyb.conference',
        'collective.cover',
        'collective.polls',
        'collective.upload',
        'five.grok',
#        'five.pt',
        'Pillow',
        'plone.app.theming',
        'Products.CMFPlone',
        'Products.PloneFormGen',
        'sc.contentrules.groupbydate',
        'sc.contentrules.layout',
        'sc.contentrules.metadata',
        'sc.social.like',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
            'plone.app.testing [robot]',
            'robotframework-wavelibrary',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
