---
file_format: mystnb
---

(gamma-function)=

# Gamma 関数

Gamma 関数は次の式であらわされる
{cite:p}`Morse1953`．

$$
\Gamma(x) = \int_0^\infty e^{-t} t^{x-1} dt
$$

特に 1 より大きい整数 $n$ については以下が成り立つ
{cite:p}`Morse1953`．

$$
\Gamma(n) = (n-1)!
$$

Gamma 関数をプロットしたものを以下に示す．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("gamma-function", version=1)
```
