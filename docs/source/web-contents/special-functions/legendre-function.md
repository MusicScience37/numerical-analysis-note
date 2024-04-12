---
file_format: mystnb
---

(legendre-function)=

# Legendre 関数

Legendre 関数は，$n=0,1,\ldots$ について次の式で表される
{cite:p}`Morse1953`．

$$
P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x - 1)^n
$$

0 から 5 次までの Legendre 関数をプロットしたものを以下に示す．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("legendre-function", version=2)
```
