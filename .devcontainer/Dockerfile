FROM registry.gitlab.com/islandoftex/images/texlive:TL2021-2022-03-13-04-43

ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client \
    gnupg2 \
    vim nano \
    python3-pip python3-venv && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    pip3 install pipx && \
    pipx install pipenv
