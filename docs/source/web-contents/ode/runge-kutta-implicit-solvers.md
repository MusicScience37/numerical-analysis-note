---
file_format: mystnb
---

# 陰的 Runge-Kutta 法で Jacobian の計算が困難な場合に使用する線形方程式のソルバーのベンチマーク

陰的 Runge-Kutta 法において，Jacobian の計算が困難な場合に方程式を解く際に使用する
線形方程式のソルバーについて，以下の解法の計算時間を測定した．

- GMRES 法（numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp` の実装）
- BiCGstab 法（numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp` の実装）

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-runge-kutta-gmres", version=1)
```

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-runge-kutta-bicgstab", version=1)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 14.0.6

## ソースコード

- 1 枚目のグラフ：
  numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
  のコミット `e7cddd677dbd031f2b2c2e8e8622a8c318f7b31b` 時点のものを使用した．

- 2 枚目のグラフ：
  numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
  のコミット `a901bef56f58e3c2cee21ad60ca258efae0f0018` 時点のものを使用した．
