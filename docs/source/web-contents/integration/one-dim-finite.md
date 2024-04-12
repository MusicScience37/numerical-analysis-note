---
file_format: mystnb
---

# 1 次元の有限区間の積分のベンチマーク

以下のような 1 次元の有限区間上の積分に数値積分を適用した．

```{math}
\int_{0}^{1} e^x dx = e - 1
```

```{math}
\int_{-1}^{1} \sqrt{1-x^2} dx = \frac{\pi}{2}
```

```{math}
\int_{-1}^{1} \frac{1}{\sqrt{1-x^2}} dx = \pi
```

## 結果

Gauss-Legendre 公式 {cite:p}`Mori1993` で
[Legendre 関数](legendre-function) の次数を上げていった場合に
計算結果の誤差がどのように変化するか実験した結果は以下のようになる．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("integ-gauss-legendre-errors", version=1)
```

Gauss-Legendre-Kronrod 公式 {cite:p}`Laurie1997` で
[Legendre 関数](legendre-function) の次数を上げていった場合に
適応積分による計算時間がどのように変化するか実験した結果は以下のようになる．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("integ-gauss-legendre-kronrod-time", version=1)
```

二重指数関数型公式 {cite:p}`Press2007` で
計算に用いる点数を増やしていった場合に
計算結果の誤差がどのように変化するか実験した結果は以下のようになる．

```{code-cell}
:tags: ["hide-input"]

from num_anal_plots.show_plot_in_jupyter import show_plot_in_jupyter

show_plot_in_jupyter("integ-de-finite-time", version=1)
```
