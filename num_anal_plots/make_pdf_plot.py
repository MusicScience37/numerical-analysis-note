"""PDF 形式のプロットを生成する。"""

import pathlib
import subprocess

import click

from num_anal_plots.plots.plots import PLOT_INFO_DICT, PLOT_NAMES, PlotInfo

THIS_DIR = pathlib.Path(__file__).absolute().parent
ROOT_DIR = THIS_DIR.parent
IMAGE_DIR = ROOT_DIR / "numerical-analysis-note" / "plots"


def _make_pdf_plot(info: PlotInfo) -> None:
    """PDF 形式のプロットを生成する。

    Args:
        info (PlotInfo): プロットの情報。
    """
    svg_path = IMAGE_DIR / f"{info.name}.svg"
    temp_pdf_path = IMAGE_DIR / f"{info.name}-temp.pdf"
    pdf_path = IMAGE_DIR / f"{info.name}.pdf"

    click.echo(f"> Creating {pdf_path}")

    figure = info.figure_factory()

    # PDF を出力させると MathJax の読み込み中の表示が画像内に出力されるため、
    # 一旦 SVG で出力させる。
    figure.write_image(str(svg_path))

    # SVG から PDF へ変換。
    # まだ埋め込まれていないフォントが使われている状態。
    subprocess.run(
        [
            "svg2pdf",
            str(svg_path),
            "-o",
            str(temp_pdf_path),
        ],
        check=True,
    )

    # テキストをパスに変換。
    subprocess.run(
        [
            "gs",
            "-dNoOutputFonts",
            "-sDEVICE=pdfwrite",
            "-o",
            str(pdf_path),
            str(temp_pdf_path),
        ],
        check=True,
    )

    # 要らなくなった中間ファイルを削除。
    svg_path.unlink()
    temp_pdf_path.unlink()


@click.command
@click.argument("names", nargs=-1)
def make_pdf_plot(names: list[str]) -> None:
    """PDF 形式のプロットを生成する。"""
    if not names:
        names = PLOT_NAMES
    for name in names:
        _make_pdf_plot(PLOT_INFO_DICT[name])

    click.echo("Finish!")


if __name__ == "__main__":
    make_pdf_plot()
