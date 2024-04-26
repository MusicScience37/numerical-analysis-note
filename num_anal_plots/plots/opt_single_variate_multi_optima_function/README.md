# 局所最適解を持つランダムな関数の最適化の最適化のベンチマーク（1 次元）

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## 実施内容

numerical-collection-cpp のコミット 08e28636c543138732298dfe715b6ab252db1e40 において，
以下のコマンドを実行した．

```bash
./build/Release/bin/num_collect_bench_opt_single_variate_multi_optima_function --compressed-msgpack bench.data --json bench.json
```
