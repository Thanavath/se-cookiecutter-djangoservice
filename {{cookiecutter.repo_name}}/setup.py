#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements

import {{ cookiecutter.app_name }}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = {{ cookiecutter.app_name }}.__version__

readme = open('README.rst').read()

session = PipSession()
requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=session)
]

setup(
    name='{{ cookiecutter.project_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.app_name }}',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)

