"""常微分方程式関連のプロットの共通パラメータの定義。"""

# 主に比較に使用するソルバー。
MAIN_SOLVERS = [
    "RKF45",
    "DOPRI5",
    "Tanaka2",
    "SDIRK4",
    "ESDIRK45c",
    "RODASP",
    "RODASPR",
    "AVF3",
    "AVF4",
]

# 陽的 Runge-Kutta 法のソルバー。
EXPLICIT_RUNGE_KUTTA_SOLVERS = [
    "RKF45",
    "DOPRI5",
    "ARK4(3)-ERK",
    "RK4",
]

# 陰的 Runge-Kutta 法のソルバー。
IMPLICIT_RUNGE_KUTTA_SOLVERS = [
    "Tanaka1",
    "Tanaka2",
    "SDIRK4",
    "ARK4(3)-ESDIRK",
    "ARK5(4)-ESDIRK",
    "ESDIRK45c",
]

# Rosenbrock 法のソルバー。
ROSENBROCK_SOLVERS = [
    "ROS3w",
    "ROS34PW3",
    "RODASP",
    "RODASPR",
]

# AVF 法のソルバー。
AVF_SOLVERS = [
    "AVF2",
    "AVF3",
    "AVF4",
]

# シンプレクティック解法のソルバー。
SYMPLECTIC_SOLVERS = [
    "LeapFrog",
    "Forest4",
]

# Runge-Kutta 法のソルバー。
RUNGE_KUTTA_SOLVERS = EXPLICIT_RUNGE_KUTTA_SOLVERS + IMPLICIT_RUNGE_KUTTA_SOLVERS

# Runge-Kutta 法以外のソルバー。
NON_RUNGE_KUTTA_SOLVERS = ROSENBROCK_SOLVERS + AVF_SOLVERS + SYMPLECTIC_SOLVERS

# ソルバーの分類。
SOLVER_TYPE_MAPPING = {name: "Runge-Kutta" for name in RUNGE_KUTTA_SOLVERS}
SOLVER_TYPE_MAPPING.update({name: "Others" for name in NON_RUNGE_KUTTA_SOLVERS})
