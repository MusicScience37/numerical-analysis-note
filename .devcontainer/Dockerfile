FROM registry.gitlab.com/musicscience37_ci/texlive-pipenv-docker:v0.1

ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client \
    gnupg2 \
    vim nano && \
    apt-get autoremove -y && \
    apt-get autoclean
