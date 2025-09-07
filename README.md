# プロジェクト概要

このリポジトリは、因果推論のための合成データセット生成と因果構造推定を行う Python スクリプト群を提供します。
主に以下のスクリプトを含みます。

- `create_dataset.py` : DAG（有向非巡回グラフ）に基づく合成データセットの生成
- `lingam_example.py` : DirectLiNGAM アルゴリズムによる因果構造の推定
- `run_all.bat` : Windows 環境で両スクリプトを連続実行するバッチファイル

---

# 環境構築手順

1. Python 3.7 以上がインストールされていることを確認してください。

2. 仮想環境を作成し、有効化します（Windows の場合）:

```bat
python -m venv venv
venv\Scripts\activate
```

3. 必要なパッケージを `requirements.txt` からインストールします:

```bat
pip install -r requirements.txt
```

4. 以上で環境構築が完了し、スクリプトを実行できるようになります。

---

# create_dataset.py の概要と使い方

`create_dataset.py` は、因果推論のための DAG（有向非巡回グラフ）を定義し、その DAG に基づいた合成データセットを生成する Python スクリプトです。

主な機能:

- スケールフリー型 DAG の生成
- 任意の隣接行列による DAG の指定
- 線形・非線形、ガウス・非ガウスなどの SEM タイプ対応の合成データ生成
- DAG の可視化（NetworkX と matplotlib 使用）
- 生成データの CSV ファイル保存

## 設定ファイル `config.json` の主なパラメータ

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

## 使い方

1. `config.json` を編集し、生成したい DAG やデータセットのパラメータを設定します。

2. ターミナルで以下のコマンドを実行します。

```bash
python create_dataset.py
```

3. 設定に基づき DAG が生成・可視化され、対応する合成データが作成されます。

4. 生成データは指定した CSV ファイルに保存されます。

---

# lingam_example.py の概要と使い方

`lingam_example.py` は、DirectLiNGAM アルゴリズムを用いて因果推論を行う Python スクリプトです。

主な機能:

- CSV ファイルから合成データセットを読み込み
- DirectLiNGAM による因果構造の推定
- 推定された DAG の可視化（NetworkX と matplotlib 使用）
- 真の DAG との比較による評価指標（SHD, F1 スコアなど）の計算
- 推定結果の CSV ファイル保存
- 複数のデータセットに対する一括処理と評価結果の集約

## 使い方

1. `res/dataset` フォルダにある合成データセット CSV ファイルと、`res/dag_GT` フォルダにある真の DAG CSV ファイルを用意します。

2. ターミナルで以下のコマンドを実行します。

```bash
python lingam_example.py
```

3. DirectLiNGAM による因果推論が実行され、推定された DAG の可視化や評価指標の計算が行われます。

4. 推定された DAG は `res/predicted_dags` フォルダに CSV ファイルとして保存され、評価指標の集約結果も同フォルダに保存されます。

---

# run_all.bat の概要と使い方

`run_all.bat` は、Windows 環境で `create_dataset.py` と `lingam_example.py` の両方のスクリプトを連続して実行するバッチファイルです。
各スクリプトの実行結果を確認し、エラーが発生した場合は処理を中断します。

## 使い方

1. ターミナル（コマンドプロンプト）を開きます。

2. プロジェクトのルートディレクトリに移動します。

3. 以下のコマンドを実行します。

```bat
run_all.bat
```

4. `create_dataset.py` と `lingam_example.py` が順に実行され、両方成功すると「Both scripts executed successfully.」と表示されます。

5. いずれかのスクリプトが失敗した場合は、エラーメッセージが表示され処理が停止します。

---

# 注意点

- `dag_type` を `'custom'` に設定する場合は、`custom_adj` に隣接行列を 2 次元リスト形式で指定してください。

- 依存ライブラリとして `numpy`, `pandas`, `networkx`, `matplotlib`, `castle` が必要です。環境構築手順に従い事前にインストールしてください。

---

# 詳細・補足

詳細は各スクリプトのソースコード内のコメントも参照してください。
