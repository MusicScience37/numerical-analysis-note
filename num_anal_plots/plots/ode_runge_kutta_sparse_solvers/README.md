# 陰的 Runge-Kutta 法で Jacobian の計算が困難な場合に使用する線形方程式のソルバーのベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## 実施内容

numerical-collection-cpp のコミット bcc66185ede6846e50b208cbd04cac2fbe8781fd において，
以下のコマンドを実行した．

```bash
./build/Release/bin/num_collect_bench_sparse_linear_equation --compressed-msgpack bench.data --json bench.json
```
