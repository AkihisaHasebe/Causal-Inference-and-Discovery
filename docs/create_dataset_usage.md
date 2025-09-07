# create_dataset.py と config.json の使い方

このドキュメントでは、`create_dataset.py` スクリプトとその設定ファイル `config.json` の概要と使い方を説明します。

---

## create_dataset.py の概要

`create_dataset.py` は、因果推論のための DAG（有向非巡回グラフ）を定義し、その DAG に基づいた合成データセットを生成する Python スクリプトです。  
主な機能は以下の通りです。

- スケールフリー型 DAG の生成
- 任意の隣接行列による DAG の指定
- DAG に基づく合成データの生成（線形・非線形、ガウス・非ガウスなどの SEM タイプ対応）
- DAG の可視化（NetworkX と matplotlib を使用）
- 生成データの CSV ファイル保存

---

## config.json の概要

`config.json` は、`create_dataset.py` の動作パラメータを外部から制御するための JSON 形式の設定ファイルです。  
主な設定項目は以下の通りです。

| パラメータ名  | 説明                                      | デフォルト値            |
| ------------- | ----------------------------------------- | ----------------------- |
| seed          | 乱数シード                                | 18                      |
| n_nodes       | ノード数（スケールフリー DAG 生成時）     | 10                      |
| n_edges       | エッジ数（スケールフリー DAG 生成時）     | 17                      |
| n_samples     | 生成するデータサンプル数                  | 10000                   |
| method        | データ生成方法（例: 'linear'）            | 'linear'                |
| sem_type      | SEM のタイプ（例: 'gauss'）               | 'gauss'                 |
| dag_type      | DAG の種類 ('scale_free' または 'custom') | 'scale_free'            |
| custom_adj    | カスタム隣接行列（dag_type が'custom'時） | null                    |
| save_filename | 生成データの保存ファイル名                | 'synthetic_dataset.csv' |

---

## 使い方

1. `config.json` を編集し、生成したい DAG やデータセットのパラメータを設定します。
2. ターミナルで以下のコマンドを実行します。

```bash
python create_dataset.py
```

3. 設定に基づき DAG が生成・可視化され、対応する合成データが作成されます。
4. 生成データは指定した CSV ファイルに保存されます。

---

## 注意点

- `dag_type` を `'custom'` に設定する場合は、`custom_adj` に隣接行列を 2 次元リスト形式で指定してください。
- 依存ライブラリとして `numpy`, `networkx`, `matplotlib`, `gCastle` が必要です。事前にインストールしてください。

---

以上が `create_dataset.py` と `config.json` の基本的な説明と使い方です。  
詳細はソースコード内のコメントも参照してください。
