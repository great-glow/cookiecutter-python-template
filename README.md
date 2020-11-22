![Main](https://github.com/great-glow/cookiecutter-python-template/workflows/Main/badge.svg)

# Cookiecutter Template for Python Projects

This template uses [Poetry](https://python-poetry.org/) as a dependency manager.

I have another similar template that uses Pipenv [here](https://github.com/VaultVulp/cookiecutter-python-template).

## Usage

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) globally
    ```bash
    pip install cookiecutter
    ```
2. Use my template
    ```bash
    cookiecutter https://github.com/great-glow/cookiecutter-python-template
    cd <project-folder>
    git init
    poetry install
    git add .
    git commit -m "Initial commit"
    ```
