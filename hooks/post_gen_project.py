#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

if __name__ == '__main__':
    process = subprocess.call(
        ['pip', 'install', '-q', 'Sphinx']
    )
    process = subprocess.call(
        [
            'sphinx-quickstart',
            '-q',
            '-p', '{{ cookiecutter.project_name }}',
            '-a', '{{ cookiecutter.full_name }}',
            '-v', '{{ cookiecutter.version }}',
            '--makefile',
            'sphinx_doc'
        ]
    )
