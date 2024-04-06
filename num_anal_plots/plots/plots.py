"""プロットの一覧。"""

import collections.abc
import dataclasses

import plotly.graph_objects

from num_anal_plots.plots.laplacian_2d_grid.laplacian_2d_grid import laplacian_2d_grid
from num_anal_plots.plots.legendre_function.legendre_function import legendre_function
from num_anal_plots.plots.ode_runge_kutta_sparse_solvers.ode_runge_kutta_sparse_solvers import (
    ode_runge_kutta_sparse_solvers,
    ode_runge_kutta_sparse_solvers_gmres,
)


@dataclasses.dataclass
class PlotInfo:
    """プロットごとの情報。"""

    name: str
    figure_factory: collections.abc.Callable[[], plotly.graph_objects.Figure]


PLOT_INFO_LIST = [
    PlotInfo(name="laplacian-2d-grid", figure_factory=laplacian_2d_grid),
    PlotInfo(
        name="ode-runge-kutta-sparse-solvers",
        figure_factory=ode_runge_kutta_sparse_solvers,
    ),
    PlotInfo(
        name="ode-runge-kutta-sparse-solvers-gmres",
        figure_factory=ode_runge_kutta_sparse_solvers_gmres,
    ),
    PlotInfo(name="legendre-function", figure_factory=legendre_function),
]

PLOT_NAMES = [info.name for info in PLOT_INFO_LIST]

PLOT_INFO_DICT = {info.name: info for info in PLOT_INFO_LIST}
