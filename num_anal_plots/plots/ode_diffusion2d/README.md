# 2次元拡散方程式による常微分方程式の数値解法のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット aada5a2ffd442f3ce90121ac78fac102a17b602d において，
以下のコマンドを実行した．

```shell
./build/Release/bin/bench_ode_diffusion2d_dirichlet results
./build/Release/bin/bench_ode_diffusion2d_neumann results
```
