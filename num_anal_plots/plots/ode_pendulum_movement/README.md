# 振り子の運動を用いた常微分方程式解法のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット aada5a2ffd442f3ce90121ac78fac102a17b602d において，
以下のコマンドを実行した．

```shell
./build/Release/bin/num_collect_bench_ode_pendulum_movement results
./build/Release/bin/num_collect_bench_ode_pendulum_movement_fixed_step results
```
