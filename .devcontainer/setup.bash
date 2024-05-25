#!/bin/bash

sudo chmod 0777 /cache_volume/
mkdir -p $POETRY_CACHE_DIR

poetry config virtualenvs.in-project true
poetry env use 3.12
poetry install

poetry run pre-commit install

git config gpg.program gpg2
git config commit.gpgsign true
git config tag.gpgsign true

git lfs install

echo "source /usr/share/bash-completion/completions/git" >>~/.bashrc
