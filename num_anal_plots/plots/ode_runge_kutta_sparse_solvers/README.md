# 陰的 Runge-Kutta 法で Jacobian の計算が困難な場合に使用する線形方程式のソルバーのベンチマーク

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット 6630c05aefc5802f289ef4b12c4bb87386e8dadf において，
以下のコマンドを実行した．

```bash
./build/Release/bin/bench_ode_sparse_linear_equation --compressed-msgpack bench.data --json bench.json
```
