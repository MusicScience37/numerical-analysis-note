"""プロットの一覧。"""

import collections.abc
import dataclasses

import plotly.graph_objects

from num_anal_plots.plots.gamma_function.gamma_function import gamma_function
from num_anal_plots.plots.integ_finite.integ_finite_de import integ_de_errors
from num_anal_plots.plots.integ_finite.integ_finite_gauss_legendre import (
    integ_gauss_legendre_errors,
)
from num_anal_plots.plots.integ_finite.integ_finite_gauss_legendre_kronrod import (
    integ_gauss_legendre_kronrod_time,
)
from num_anal_plots.plots.laplacian_2d_grid.laplacian_2d_grid import laplacian_2d_grid
from num_anal_plots.plots.legendre_function.legendre_function import legendre_function
from num_anal_plots.plots.ode_kaps_problem.ode_kaps_problem import (
    ode_kaps_problem_work_error,
)
from num_anal_plots.plots.ode_pendulum_movement.ode_pendulum_movement_auto_step import (
    ode_pendulum_movement_auto_step_all_work_error,
    ode_pendulum_movement_auto_step_work_error,
)
from num_anal_plots.plots.ode_pendulum_movement.ode_pendulum_movement_fixed_step import (
    ode_pendulum_movement_fixed_step_work_error,
)
from num_anal_plots.plots.ode_runge_kutta_sparse_solvers.ode_runge_kutta_sparse_solvers import (
    ode_runge_kutta_sparse_solvers,
    ode_runge_kutta_sparse_solvers_gmres,
)
from num_anal_plots.plots.opt_convex_difficult_functions.opt_convex_difficult_functions import (
    opt_convex_difficult_functions_evaluations,
    opt_convex_difficult_functions_time,
)
from num_anal_plots.plots.opt_multi_variate_difficult_multi_optima_function.opt_multi_variate_difficult_multi_optima_function import (
    opt_multi_variate_difficult_multi_optima_function_evaluations,
    opt_multi_variate_difficult_multi_optima_function_time,
)
from num_anal_plots.plots.opt_random_multi_quadratic_function.opt_random_multi_quadratic_function import (
    opt_random_multi_quadratic_function_evaluations,
    opt_random_multi_quadratic_function_time,
)
from num_anal_plots.plots.opt_single_variate_multi_optima_function.opt_single_variate_multi_optima_function import (
    opt_single_variate_multi_optima_function_evaluations,
    opt_single_variate_multi_optima_function_time,
)
from num_anal_plots.plots.rbf_wendland_csrbf.rbf_wendland_csrbf import (
    rbf_wendland_csrbf,
)


@dataclasses.dataclass
class PlotInfo:
    """プロットごとの情報。"""

    name: str
    figure_factory: collections.abc.Callable[[], plotly.graph_objects.Figure]


PLOT_INFO_LIST = [
    # Linear Solvers.
    PlotInfo(name="laplacian-2d-grid", figure_factory=laplacian_2d_grid),
    # ODE Solvers.
    PlotInfo(
        name="ode-runge-kutta-sparse-solvers",
        figure_factory=ode_runge_kutta_sparse_solvers,
    ),
    PlotInfo(
        name="ode-runge-kutta-sparse-solvers-gmres",
        figure_factory=ode_runge_kutta_sparse_solvers_gmres,
    ),
    PlotInfo(
        name="ode-pendulum-movement-auto-step-work-error",
        figure_factory=ode_pendulum_movement_auto_step_work_error,
    ),
    PlotInfo(
        name="ode-pendulum-movement-auto-step-all-work-error",
        figure_factory=ode_pendulum_movement_auto_step_all_work_error,
    ),
    PlotInfo(
        name="ode-pendulum-movement-fixed-step-work-error",
        figure_factory=ode_pendulum_movement_fixed_step_work_error,
    ),
    PlotInfo(
        name="ode-kaps-problem-work-error",
        figure_factory=ode_kaps_problem_work_error,
    ),
    # Special Functions.
    PlotInfo(name="legendre-function", figure_factory=legendre_function),
    PlotInfo(name="gamma-function", figure_factory=gamma_function),
    # RBF interpolation
    PlotInfo(name="rbf-wendland-csrbf", figure_factory=rbf_wendland_csrbf),
    # Numerical integration.
    PlotInfo(
        name="integ-gauss-legendre-errors",
        figure_factory=integ_gauss_legendre_errors,
    ),
    PlotInfo(
        name="integ-gauss-legendre-kronrod-time",
        figure_factory=integ_gauss_legendre_kronrod_time,
    ),
    PlotInfo(
        name="integ-de-finite-time",
        figure_factory=integ_de_errors,
    ),
    # Optimization.
    PlotInfo(
        name="opt-random-multi-quadratic-function-time",
        figure_factory=opt_random_multi_quadratic_function_time,
    ),
    PlotInfo(
        name="opt-random-multi-quadratic-function-evaluations",
        figure_factory=opt_random_multi_quadratic_function_evaluations,
    ),
    PlotInfo(
        name="opt-convex-difficult-functions-time",
        figure_factory=opt_convex_difficult_functions_time,
    ),
    PlotInfo(
        name="opt-convex-difficult-functions-evaluations",
        figure_factory=opt_convex_difficult_functions_evaluations,
    ),
    PlotInfo(
        name="opt-single-variate-multi-optima-function-time",
        figure_factory=opt_single_variate_multi_optima_function_time,
    ),
    PlotInfo(
        name="opt-single-variate-multi-optima-function-evaluations",
        figure_factory=opt_single_variate_multi_optima_function_evaluations,
    ),
    PlotInfo(
        name="opt-multi-variate-difficult-multi-optima-function-time",
        figure_factory=opt_multi_variate_difficult_multi_optima_function_time,
    ),
    PlotInfo(
        name="opt-multi-variate-difficult-multi-optima-function-evaluations",
        figure_factory=opt_multi_variate_difficult_multi_optima_function_evaluations,
    ),
]

PLOT_NAMES = [info.name for info in PLOT_INFO_LIST]

PLOT_INFO_DICT = {info.name: info for info in PLOT_INFO_LIST}
