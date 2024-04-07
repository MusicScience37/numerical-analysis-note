---
file_format: mystnb
---

# 陰的 Runge-Kutta 法における線形方程式のソルバーのベンチマーク

陰的 Runge-Kutta 法において，Jacobian の計算が困難な場合に方程式を解く際に使用する
線形方程式のソルバーについて，以下の解法の計算時間を測定した．

- GMRES 法 {cite:p}`Golub2013` {cite:p}`Blom2013`
  （numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp` の実装）
- BiCGstab 法 {cite:p}`Golub2013`
  （numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp` の実装）

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-runge-kutta-sparse-solvers", version=4)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `bcc66185ede6846e50b208cbd04cac2fbe8781fd` 時点のものを使用した．
