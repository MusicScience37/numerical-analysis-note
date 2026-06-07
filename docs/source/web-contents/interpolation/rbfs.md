---
file_format: mystnb
---

# RBF のプロット

## パラメータのない RBF

パラメータのない RBF をいくつかプロットしたものを以下に示す．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("rbf-general-rbfs", version=2)
```

## Bessel RBF

Bessel RBF をいくつかプロットしたものを以下に示す．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("rbf-bessel-rbf", version=2)
```

## Polyharmonic Spline RBF

Polyharmonic spline RBF をいくつかプロットしたものを以下に示す．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("rbf-polyharmonic-spline-rbf", version=2)
```

## Wendland の Compactly Supported RBF

Wendland の Compactly Supported RBF $\varphi_{l,k}(r)$ {cite:p}`Wendland1995` を
いくつかプロットしたものを以下に示す．

```{code-cell}
:tags: ["remove-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("rbf-wendland-csrbf", version=3)
```
