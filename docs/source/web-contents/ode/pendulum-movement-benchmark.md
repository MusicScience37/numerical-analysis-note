---
file_format: mystnb
---

# 振り子の運動を用いた常微分方程式解法のベンチマーク

振り子の角度 $\theta$ に関する運動方程式

$$
\ddot{\theta} = -\sin{\theta}
$$

に対して常微分方程式のソルバーを適用し，計算時間と誤差を測定した．

## ステップ幅の自動調整付きのソルバーに対するベンチマーク結果

ステップ幅の自動調整機能 {cite:p}`Gustafsson1991` 付きで実装したソルバーについてベンチマークを行った．

時刻 $t=0$ における初期値をもとに時刻 $t=10$ における解を求める時間と精度を測定した．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-pendulum-movement-auto-step-all-work-error", version=3)
```

## ステップ幅固定のソルバーに対するベンチマーク結果

固定のステップ幅による数値解法を実装したソルバーについてベンチマークを行った．

時刻 $t=0$ における初期値をもとに時刻 $t=100$ における解を求める時間と精度を測定した．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-pendulum-movement-fixed-step-work-error", version=3)
```

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `1ab776c2c47780ad0e2433dc4d70fe4d336abee1` 時点のものを使用した．
