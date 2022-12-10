# Docker イメージの変更

Docker イメージの変更時は以下を更新する．

- `.gitlab-ci.yml` の `image` 欄
- `.devcontainer/Dockerfile`

使用している TeXLive の Docker イメージは，
[TeXLive 用の Docker イメージ](https://gitlab.com/MusicScience37Projects/docker/texlive-pipenv-docker/container_registry/)
から選択している．
