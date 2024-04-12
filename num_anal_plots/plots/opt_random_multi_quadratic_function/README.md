# ランダムな係数による二次関数の最適化のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## 実施内容

numerical-collection-cpp のコミット 529081ff85e9b43f443d654b2f97cdec2a56cba4 において，
以下のコマンドを実行した．

```bash
./build/Release/bin/num_collect_bench_opt_random_multi_quadratic_function --compressed-msgpack bench.data --json bench.json
```
