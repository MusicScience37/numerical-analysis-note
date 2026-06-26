# 2次元拡散方程式による常微分方程式の数値解法のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) Ultra 5 125H
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット 1ab776c2c47780ad0e2433dc4d70fe4d336abee1 において，
以下のコマンドを実行した．

```shell
./build/Release/bin/bench_ode_diffusion2d_dirichlet results
./build/Release/bin/bench_ode_diffusion2d_neumann results
```
