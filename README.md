# 数値解析ノート

数値解析で調査したことをまとめる．

## ビルド済み PDF

- [main ブランチの最新版の PDF](https://numanalnote.musicscience37.com/numerical-analysis-note.pdf)

## 開発者向け

[dev ディレクトリ](./dev/index.md)
に本リポジトリの開発者向けのドキュメントを記載していく．

### 開発者向け注意点

**知らないと解決に時間のかかる問題もあるため，このリポジトリを clone する前に必ず読むこと．**

- 必ず **Git LFS がインストールされていることを確認してから** clone すること．
  - Git LFS を有効にした環境で clone しないと画像が読み込めない．
    そのままビルドを行おうとすると，
    BoundingBox の自動生成に対応した dvipdfmx を使用しているのに「no BoundingBox」のエラーになる．
