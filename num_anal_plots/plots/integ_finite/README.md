# 有限区間における積分のベンチマーク

## 環境

- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- コンパイラ：Clang 17.0.2

## 実施内容

numerical-collection-cpp のコミット 529081ff85e9b43f443d654b2f97cdec2a56cba4 において，
以下のコマンドを実行した．

```shell
./build/Release/bin/num_collect_bench_integ_exp --compressed-msgpack exp.data --json exp.json
./build/Release/bin/num_collect_bench_integ_sqrt_1mx2 --compressed-msgpack sqrt_1mx2.data --json sqrt_1mx2.json
./build/Release/bin/num_collect_bench_integ_inv_sqrt_1mx2 --compressed-msgpack inv_sqrt_1mx2.data --json inv_sqrt_1mx2.json
```
