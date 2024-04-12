---
file_format: mystnb
---

# テスト用の凸関数の最適化

テスト用の以下の凸関数の最適化を行う時間と関数の値を評価した回数を計測した．

- Rosenbrock function {cite:p}`GOTestProblems`
- 4 次元の Powell function {cite:p}`GOTestProblems`

## 結果

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("opt-convex-difficult-functions-time", version=2)
```

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("opt-convex-difficult-functions-evaluations", version=2)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `529081ff85e9b43f443d654b2f97cdec2a56cba4` 時点のものを使用した．
