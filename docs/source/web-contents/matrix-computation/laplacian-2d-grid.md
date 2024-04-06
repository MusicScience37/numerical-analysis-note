---
file_format: mystnb
---

# 2 次元格子上の Laplacian を離散化した方程式を解くベンチマーク

2 次元格子上で Laplacian を離散化して得られる方程式を以下の手法で解いた際の時間を計測した．

- CG 法（Eigen ライブラリ {cite:p}`EigenLibrary` を使用）
- BiCGstab 法（Eigen ライブラリ {cite:p}`EigenLibrary` を使用）

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("laplacian-2d-grid", version=2)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 14.0.6

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `d0595598d5e28bd6a6a90d3605791d391c1a61ba` 時点のものを使用した．
