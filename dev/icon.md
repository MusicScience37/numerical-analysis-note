# アイコンについて

## アイコンの作成手順

1. `icon-logo/design/icon.svg` を Inkscape で開いて編集する．
2. Inkscape で以下を出力する．
   - `icon-logo/icon512.png` (PNG 形式，512x512 ピクセル)
   - `icon-logo/icon.svg` （最適化した SVG 形式）
3. `scripts/convert-icons.sh` を実行して，以下を生成する．
   - `icon-logo/icon192.png` (PNG 形式，192x192 ピクセル)
   - `icon-logo/icon.ico` (ICO 形式)

## アイコンのサイズ

| サイズ | 用途            |
| -----: | :-------------- |
|     16 | Favicon         |
|     32 | Favicon         |
|     48 | Favicon         |
|     64 | Favicon         |
|    192 | GitLab アイコン |
