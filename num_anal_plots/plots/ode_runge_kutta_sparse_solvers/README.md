# 陰的 Runge-Kutta 法で Jacobian の計算が困難な場合に使用する線形方程式のソルバーのベンチマーク

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット 1ab776c2c47780ad0e2433dc4d70fe4d336abee1 において，
以下のコマンドを実行した．

```bash
./build/Release/bin/bench_ode_sparse_linear_equation --compressed-msgpack bench.data --json bench.json
```
