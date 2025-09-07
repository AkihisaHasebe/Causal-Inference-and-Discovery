# LinGAM に関する情報整理

## LinGAM とは

- LiNGAM (Linear Non-Gaussian Acyclic Model) は、線形の非ガウス性を仮定した因果探索モデル。
- 非ガウス性の独立成分分析(ICA)を用いて因果構造を推定する。
- 線形回帰と残差の非ガウス性を利用して因果方向を特定する。

## データ生成例

- ガウス分布と非ガウス分布の 2 種類のデータを生成し、線形回帰で因果方向を推定。
- ガウス分布の場合は因果方向の判別が難しいが、非ガウス分布の場合は LinGAM が有効。

## LinGAM の実装例（gCastle ライブラリ利用）

- `ICALiNGAM` クラスを用いて LinGAM モデルをインスタンス化し、`learn` メソッドで学習。
- `DirectLiNGAM` クラスも利用可能で、こちらも同様に `learn` メソッドで学習。
- 学習後、`causal_matrix` で推定された因果行列を取得可能。
- `weight_causal_matrix` で重み付きの因果行列を取得可能。

## パラメータ設定例

- `ICALiNGAM` の `max_iter` パラメータで最大反復回数を設定可能。
- `random_state` で乱数シードを固定し、再現性を確保。

## 可視化

- `GraphDAG` クラスを用いて推定された因果グラフを可視化。
- 真の DAG と推定 DAG の比較が可能。

## 性能評価

- `MetricsDAG` クラスを用いて、FDR, Recall, Precision, F1 スコア, SHD などの指標を計算。

## まとめ

- LinGAM は非ガウス性を利用した線形因果探索手法であり、非ガウス分布のデータに対して有効。
- gCastle ライブラリの `ICALiNGAM` と `DirectLiNGAM` クラスで簡単に実装・学習・評価が可能。
- パラメータ調整や可視化もサポートされているため、実験や解析に便利。
