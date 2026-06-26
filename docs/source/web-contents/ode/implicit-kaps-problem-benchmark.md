---
file_format: mystnb
---

# 陰的な Kaps の問題を用いた微分代数方程式に対する常微分方程式解法のベンチマーク

Kaps の問題

```{math}
\varepsilon \dot{y_1} & = -(1 + 2 \varepsilon) y_1 + y_2^2 \\
\dot{y_2} &= y_1 - y_2 - y_2^2
```

はパラメータ $\varepsilon$ が小さいほど数値解を求めるのが困難になる硬い系になり，
$\varepsilon = 0$ で微分代数方程式になる．
そこで，$\varepsilon = 0$ も含めた異なる $\varepsilon$ の値における数値解法の性能の比較を行った．

## 結果

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-implicit-kaps-problem-work-error", version=6)
```

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `1ab776c2c47780ad0e2433dc4d70fe4d336abee1` 時点のものを使用した．
