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
    # plt.show()  # GUI表示を無効化して高速化

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from castle.algorithms import DirectLiNGAM
from castle.common import GraphDAG

import pandas as pd
from evaluation_utils import evaluate_dag_estimation


def main():
    import os
    dataset_dir = 'res/dataset'
    dag_dir = 'res/dag_GT'
    pred_dir = 'res/predicted_dags'
    os.makedirs(pred_dir, exist_ok=True)

    dataset_files = sorted([f for f in os.listdir(dataset_dir) if f.startswith('synthetic_dataset_seed') and f.endswith('.csv')])
    dag_files = sorted([f for f in os.listdir(dag_dir) if f.startswith('dag_seed') and f.endswith('.csv')])

    # 評価指標を格納するリスト
    metrics_list = []

    for dataset_file, dag_file in zip(dataset_files, dag_files):
        print(f"\nProcessing dataset: {dataset_file} with true DAG: {dag_file}")

        data_path = os.path.join(dataset_dir, dataset_file)
        dag_path = os.path.join(dag_dir, dag_file)

        # データ読み込み
        data_df = pd.read_csv(data_path)
        data = data_df.values
        columns = data_df.columns

        # 真のDAG読み込み
        true_dag_df = pd.read_csv(dag_path, index_col=0)
        true_dag = true_dag_df.values

        # DirectLiNGAMで学習
        directlingam_model = fit_directlingam(data)
        print("DirectLiNGAM causal matrix:")
        print(directlingam_model.causal_matrix)
        print("DirectLiNGAM weight causal matrix:")
        print(directlingam_model.weight_causal_matrix)
        plot_graph(directlingam_model.causal_matrix, title=f'DirectLiNGAM Estimated DAG for {dataset_file}')

        # 評価指標計算を関数化して呼び出し
        metrics = evaluate_dag_estimation(directlingam_model.causal_matrix, true_dag)

        # 評価指標をリストに追加
        metrics_list.append({
            'dataset_file': dataset_file,
            'shd': metrics['shd'],
            'F1': metrics['F1']
        })

        # 推論結果をCSV保存
        pred_dag_df = pd.DataFrame(directlingam_model.causal_matrix, index=columns, columns=columns)
        save_path = os.path.join(pred_dir, f'pred_dag_{dataset_file}')
        pred_dag_df.to_csv(save_path)
        print(f"Predicted DAG saved to {save_path}")
    # すべての評価指標をまとめてCSV保存
    summary_path = os.path.join(pred_dir, 'summary_metrics.csv')
    summary_df = pd.DataFrame(metrics_list)
    summary_df.to_csv(summary_path, index=False)
    print(f"\nSummary metrics saved to {summary_path}")

if __name__ == "__main__":
    main()