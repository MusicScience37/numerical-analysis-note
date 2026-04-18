# 陰的 Runge-Kutta 法で Jacobian の計算が困難な場合に使用する線形方程式のソルバーのベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット aada5a2ffd442f3ce90121ac78fac102a17b602d において，
以下のコマンドを実行した．

```bash
./build/Release/bin/bench_ode_sparse_linear_equation --compressed-msgpack bench.data --json bench.json
```
