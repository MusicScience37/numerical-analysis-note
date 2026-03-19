FROM musicscience37/pipenv:noble

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    openssh-client \
    gnupg2 \
    vim nano \
    graphviz \
    sudo \
    # For icon conversion
    imagemagick \
    # For rsvg-converter
    librsvg2-bin \
    # For qpdf
    qpdf \
    # For configuration of locale
    locales \
    # TexLive and some related packages
    texlive-base \
    texlive-extra-utils \
    lmodern \
    fonts-ipaexfont \
    # Packages needed for tectonic
    libssl-dev \
    libgraphite2-dev \
    libharfbuzz-dev \
    libicu-dev \
    libfontconfig-dev \
    libfreetype-dev \
    && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    # Create $USERNAME user.
    # groupadd --gid $USER_GID $USERNAME && \
    # useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    # Make $USERNAME user able to use sudo command.
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME && \
    # Allow use of pyenv from $USERNAME user.
    chmod 0777 /root && \
    chmod -R 0777 /root/.pyenv && \
    # Configure locale
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8 && \
    # Install tectonic
    wget -q https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz && \
    tar -xf tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz -C /usr/local/bin/ && \
    rm tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz && \
    chmod +x /usr/local/bin/tectonic
ENV LANG=en_US.UTF-8

# Prepare poetry for $USERNAME user.
USER $USERNAME
WORKDIR /home/$USERNAME
ENV PATH="/home/$USERNAME/.local/bin:$PATH"
RUN pipx install poetry
