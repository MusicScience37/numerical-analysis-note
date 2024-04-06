---
file_format: mystnb
---

# Kaps の問題を用いた硬い系に対する常微分方程式解法のベンチマーク

Kaps の問題

```{math}
\dot{y_1} & = -(\varepsilon^{-1} + 2) y_1 + \varepsilon^{-1} y_2^2 \\
\dot{y_2} &= y_1 - y_2 - y_2^2
```

はパラメータ $\varepsilon$ が小さいほど数値解を求めるのが困難になる硬い系になる．
そこで，異なる $\varepsilon$ の値における数値解法の性能の比較を行った．

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-kaps-problem-work-error", version=2)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `f4488124c9121787879ed70a0975523e4b545586` 時点のものを使用した．
