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
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-kaps-problem-work-error", version=5)
```

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `1ab776c2c47780ad0e2433dc4d70fe4d336abee1` 時点のものを使用した．
