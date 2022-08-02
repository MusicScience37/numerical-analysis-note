FROM registry.gitlab.com/musicscience37/texlive-pipenv-docker:tl2022

ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client \
    gnupg2 \
    vim nano \
    graphviz && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*
