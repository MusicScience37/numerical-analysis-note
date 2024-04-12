# 難しいテスト用の凸関数の最適化のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## 実施内容

numerical-collection-cpp のコミット 529081ff85e9b43f443d654b2f97cdec2a56cba4 において，
以下のコマンドを実行した．

```bash
./build/Release/bin/num_collect_bench_opt_rosenbrock_function --compressed-msgpack rosenbrock_function.data --json rosenbrock_function.json
./build/Release/bin/num_collect_bench_opt_powell4_function --compressed-msgpack powell4_function.data --json powell4_function.json
```
