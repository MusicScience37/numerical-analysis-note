# 陰的な Kaps の問題を用いた常微分方程式解法のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 21.1.8

## 実施内容

numerical-collection-cpp のコミット 369425a4ec99515c58f9c04ed0209d9683d45d8b において，
以下のコマンドを実行した．

```shell
./build/Release/bin/bench_ode_implicit_kaps_problem results
```
