__version__ = '{{ cookiecutter.version }}'
default_app_config = '{{ cookiecutter.app_name }}.config.{{ cookiecutter.app_name|replace("_", " ")|title|replace(" ", "") }}Config'
