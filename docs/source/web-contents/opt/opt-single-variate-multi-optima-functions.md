---
file_format: mystnb
---

# 局所最適解を持つランダムな関数の最適化の最適化のベンチマーク（1 次元）

ランダムな係数を用いて複数の局所最適解をもつ関数を生成し
最適化を行う時間と関数の値を評価した回数を計測した．

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("opt-single-variate-multi-optima-function-time", version=2)
```

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("opt-single-variate-multi-optima-function-evaluations", version=2)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `08e28636c543138732298dfe715b6ab252db1e40` 時点のものを使用した．
