import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from castle.algorithms import DirectLiNGAM
from castle.common import GraphDAG

import pandas as pd

def load_data_from_csv(filepath):
    df = pd.read_csv(filepath)
    return df.values

# ICALiNGAM関連の関数は削除しました

def fit_directlingam(data):
    model = DirectLiNGAM()
    model.learn(data)
    return model

def plot_graph(dag_matrix, title='Estimated DAG'):
    g = nx.DiGraph(dag_matrix)
    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels=True, node_color='#00B0F0', node_size=800, arrowsize=20, font_size=14, font_color='white')
    plt.title(title)
    plt.show()

import pandas as pd
from castle.metrics import MetricsDAG

def main():
    # CSVファイルからデータ読み込み
    data = load_data_from_csv('res/synthetic_dataset.csv')
    # 列名取得
    data_df = pd.read_csv('res/synthetic_dataset.csv')
    columns = data_df.columns

    # 真のDAG読み込み
    true_dag_df = pd.read_csv('res/dag.csv', index_col=0)
    true_dag = true_dag_df.values

    # DirectLiNGAMで学習
    directlingam_model = fit_directlingam(data)
    print("DirectLiNGAM causal matrix:")
    print(directlingam_model.causal_matrix)
    print("DirectLiNGAM weight causal matrix:")
    print(directlingam_model.weight_causal_matrix)
    plot_graph(directlingam_model.causal_matrix, title='DirectLiNGAM Estimated DAG')

    # 評価指標計算
    print("\nEvaluation Metrics:")
    metrics = MetricsDAG(directlingam_model.causal_matrix, true_dag)
    print(f"DirectLiNGAM SHD: {metrics.metrics['shd']}")
    print(f"DirectLiNGAM F1 Score: {metrics.metrics['F1']}")

    # 推論結果をCSV保存
    import os
    pred_dag_df = pd.DataFrame(directlingam_model.causal_matrix, index=columns, columns=columns)
    save_path = os.path.join('res', f'pred_dag_synthetic_dataset.csv')
    pred_dag_df.to_csv(save_path)
    print(f"Predicted DAG saved to {save_path}")

if __name__ == "__main__":
    main()