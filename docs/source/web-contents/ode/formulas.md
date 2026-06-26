# 実装した常微分方程式解法の一覧

本サイトのプロットでは常微分方程式解法における公式の名称について略称を使用している．
その略称と公式の対応関係を以下に示す．

- Runge-Kutta 法
  - 陽的公式
    - `RK4`：古典的な 4 次の Runge-Kutta 法 {cite:p}`Mitsui1993`
    - `RKF45`：RKF (Runge-Kutta-Fehlberg) 45 公式 {cite:p}`Mitsui1993`
    - `DOPRI5`：DOPRI5 公式 {cite:p}`Hairer1991`
    - `ARK4(3)-ERK`：ARK4(3)6L[2]SA-ERK 公式 {cite:p}`Kennedy2003`
  - 半陰的公式
    - `ImplicitEuler`：陰的 Euler 法
    - `CrankNicolson`：Crank-Nicolson 法
    - `Tanaka1`：田中 Formula1 公式 {cite:p}`Togawa2007`
    - `Tanaka2`：田中 Formula2 公式 {cite:p}`Togawa2007`
    - `SDIRK4`：4 次の SDIRK (Singly Diagonally Implicit Runge-Kutta) 法 {cite:p}`Hairer1991`
    - `SDIRK6`：SDIRK(9,6)[1]SAL-[(9,5)A] 公式 {cite:p}`Alamri2023`
    - `ARK4(3)-ESDIRK`：ARK4(3)6L[2]SA-ESDIRK 公式 {cite:p}`Kennedy2003`
    - `ARK5(4)-ESDIRK`：ARK5(4)6L[2]SA-ESDIRK 公式 {cite:p}`Kennedy2003`
    - `ESDIRK32a`：ESDIRK 3/2 a 公式 {cite:p}`Kvaerno2004`
    - `ESDIRK45c`：ESDIRK45c 公式 {cite:p}`Jorgensen2018`
  - 陰的公式
    - `LobattoIIIC4`：Lobatto IIIC 4 次の公式 {cite:p}`Hairer1991`
    - `LobattoIIIC6`：Lobatto IIIC 6 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA3`：Radau IIA 3 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA5`：Radau IIA 5 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA7`：Radau IIA 7 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA9`：Radau IIA 9 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA13`：Radau IIA 13 次の公式 {cite:p}`Hairer1991`
    - `RadauIIA17`：Radau IIA 17 次の公式 {cite:p}`Hairer1991`
- Rosenbrock 法
  - `ROS3w`：ROS3w 公式 {cite:p}`Rang2005`
  - `ROS3Dw`：ROS3Dw 公式 {cite:p}`Rang2005`
  - `ROS3PRL2`：ROS3PRL2 公式 {cite:p}`Rang2015`
  - `ROS34PRw`：ROS34PRw 公式 {cite:p}`Rang2015`
  - `ROS34PW3`：ROS34PW3 公式 {cite:p}`Rang2005`
  - `RODASP`：RODASP 公式 {cite:p}`Steinebach2022`
  - `RODASPR`：RODASPR 公式 {cite:p}`Rang2015`
- 平均ベクトル場法 {cite:p}`Quispel2008`
  - `AVF2`：2 次の解法
  - `AVF3`：3 次の解法
  - `AVF4`：4 次の解法
- シンプレクティック積分法
  - 陽的公式
    - `LeapFrog`：Leap-frog 法 {cite:p}`Forest1990`
    - `Forest4`：{cite:p}`Forest1990` における 4 次の公式
