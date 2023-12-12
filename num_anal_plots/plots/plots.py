"""プロットの一覧。"""

import collections.abc
import dataclasses

import plotly.graph_objects

from num_anal_plots.plots.laplacian_2d_grid.laplacian_2d_grid import laplacian_2d_grid
from num_anal_plots.plots.ode_runge_kutta_gmres.ode_runge_kutta_gmres import (
    ode_runge_kutta_gmres,
)
from num_anal_plots.plots.ode_runge_kutta_bicgstab.ode_runge_kutta_bicgstab import (
    ode_runge_kutta_bicgstab,
)


@dataclasses.dataclass
class PlotInfo:
    """プロットごとの情報。"""

    name: str
    figure_factory: collections.abc.Callable[[], plotly.graph_objects.Figure]


PLOT_INFO_LIST = [
    PlotInfo(name="laplacian-2d-grid", figure_factory=laplacian_2d_grid),
    PlotInfo(name="ode-runge-kutta-gmres", figure_factory=ode_runge_kutta_gmres),
    PlotInfo(name="ode-runge-kutta-bicgstab", figure_factory=ode_runge_kutta_bicgstab),
]

PLOT_NAMES = [info.name for info in PLOT_INFO_LIST]

PLOT_INFO_DICT = {info.name: info for info in PLOT_INFO_LIST}
