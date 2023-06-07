# 2 次元格子上の Laplacian を用いたベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 14.0.6

## 実施内容

numerical-collection-cpp のコミット d0595598d5e28bd6a6a90d3605791d391c1a61ba において，
以下のコマンドを実行した．

```bash
./build/Release/bin/num_collect_bench_laplacian_2d_grid --msgpack bench.data --json bench.json
```
