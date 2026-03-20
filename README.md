# 数値解析ノート

[![pipeline status](https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-analysis-note/badges/main/pipeline.svg)](https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-analysis-note/-/commits/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

数値解析関係で調査したことをまとめたノートです．

ノートの最新版の PDF は
[こちら](https://numanalnote.musicscience37.com/numerical-analysis-note.pdf)
で確認できます．

また，インタラクティブなグラフを含む
[Web ページ](https://numanalnote.musicscience37.com/)
も用意しています．

## リポジトリ

- [GitLab（メイン）](https://gitlab.com/MusicScience37Projects/numerical-analysis/numerical-analysis-note)
- [GitHub（ミラー）](https://github.com/MusicScience37/numerical-analysis-note)

## 成果物

- [ノート (PDF)](https://numanalnote.musicscience37.com/numerical-analysis-note.pdf)
- [Web ページ](https://numanalnote.musicscience37.com/)

## 開発者向け

[dev ディレクトリ](./dev/index.md)
に本リポジトリの開発者向けのドキュメントを記載していく．

### 環境構築の概要

1. VSCode の DevContainer を起動する．
2. Python の仮想環境を準備する．

   ```shell
   cd <repository-root>
   poetry sync
   ```

### その他のコマンド

- TeX 文書用の画像を生成する．

  ```shell
  cd <repository-root>
  ./scripts/generate-images.sh
  ```

- 上記の画像生成が済んだ状態で TeX の文書をビルドする．

  ```shell
  cd numerical-analysis-note
  ./build.sh
  ```

- Web ページをビルドしてプレビューする．

  ```shell
  cd <repository-root>
  ./docs/start-auto-build.sh
  ```
