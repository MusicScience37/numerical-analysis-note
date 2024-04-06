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

以下の公式を用い，ステップ幅の自動調整機能 {cite:p}`Gustafsson1991` 付きで実装したソルバーについてベンチマークを行った．

- Runge-Kutta 法
  - 陽的公式
    - `RKF45`：RKF (Runge-Kutta-Fehlberg) 45 公式 {cite:p}`Mitsui1993`
    - `DOPRI5`：DOPRI5 公式 {cite:p}`Hairer1991`
    - `ARK4(3)-ERK`：ARK4(3)6L[2]SA-ERK 公式 {cite:p}`Kennedy2003`
  - 半陰的公式
    - `Tanaka1`：田中 Formula1 公式 {cite:p}`Togawa2007`
    - `Tanaka2`：田中 Formula2 公式 {cite:p}`Togawa2007`
    - `SDIRK4`：4 次の SDIRK (Singly Diagonally Implicit Runge-Kutta) 法 {cite:p}`Hairer1991`
    - `ARK4(3)-ESDIRK`：ARK4(3)6L[2]SA-ESDIRK 公式 {cite:p}`Kennedy2003`
    - `ARK5(4)-ESDIRK`：ARK5(4)6L[2]SA-ESDIRK 公式 {cite:p}`Kennedy2003`
    - `ESDIRK45c`：ESDIRK45c 公式 {cite:p}`Jorgensen2018`
- Rosenbrock 法
  - `ROS3w` 公式：ROS3w 公式 {cite:p}`Rang2005`
  - `ROS34PW3` 公式：ROS3w 公式 {cite:p}`Rang2005`
  - `RODASP` 公式：RODASP 公式 {cite:p}`Steinebach2022`
  - `RODASPR` 公式：RODASPR 公式 {cite:p}`Rang2015`
- 平均ベクトル場法 {cite:p}`Quispel2008`
  - `AVF2`：2 次の解法
  - `AVF3`：3 次の解法
  - `AVF4`：4 次の解法

時刻 $t=0$ における初期値をもとに時刻 $t=10$ における解を求める時間と精度を測定した．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-pendulum-movement-auto-step-all-work-error", version=1)
```

## ステップ幅固定のソルバーに対するベンチマーク結果

以下の公式を用い，固定のステップ幅による数値解法を実装したソルバーについてベンチマークを行った．

- Runge-Kutta 法
  - 陽的公式
    - `RK4`：古典的な 4 次の Runge-Kutta 法 {cite:p}`Mitsui1993`
- シンプレクティック積分法
  - 陽的公式
    - `LeapFrog`：Leap-frog 法 {cite:p}`Forest1990`
    - `Forest4`：{cite:p}`Forest1990` における 4 次の公式
- AVF (Average Vector Field) 法 {cite:p}`Quispel2008`
  - `AVF2`：2 次の解法
  - `AVF3`：3 次の解法
  - `AVF4`：4 次の解法

時刻 $t=0$ における初期値をもとに時刻 $t=100$ における解を求める時間と精度を測定した．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("ode-pendulum-movement-fixed-step-work-error", version=1)
```

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## ソースコード

numerical-collection-cpp リポジトリ {cite:p}`NumericalCollectionCpp`
のコミット `f4488124c9121787879ed70a0975523e4b545586` 時点のものを使用した．
