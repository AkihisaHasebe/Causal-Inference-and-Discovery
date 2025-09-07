import os
import json
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from castle.datasets import DAG, IIDSimulation
import glob

def load_config(config_path):
    """
    Load configuration parameters from a JSON file.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def generate_scale_free_dag(n_nodes=10, n_edges=17, seed=18):
    """
    Generate a scale-free DAG adjacency matrix.
    """
    adj_matrix = DAG.scale_free(n_nodes=n_nodes, n_edges=n_edges, seed=seed)
    return adj_matrix

def generate_custom_dag(adj_matrix):
    """
    Accept a custom adjacency matrix and return it as a DAG.
    """
    return adj_matrix

def simulate_data(dag_matrix, n_samples=10000, method='linear', sem_type='gauss'):
    """
    Generate synthetic data based on the given DAG adjacency matrix.
    """
    dataset = IIDSimulation(W=dag_matrix, n=n_samples, method=method, sem_type=sem_type)
    return dataset.X

def visualize_dag(adj_matrix, title='DAG Visualization'):
    """
    Visualize the DAG using networkx and matplotlib.
    """
    g = nx.DiGraph(adj_matrix)
    plt.figure(figsize=(12, 8))
    nx.draw(
        G=g,
        node_color='#00B0F0',
        node_size=1200,
        arrowsize=17,
        with_labels=True,
        font_color='white',
        font_size=21,
        pos=nx.circular_layout(g)
    )
    plt.title(title)
    plt.show()

def save_data(data, filename='dataset.csv'):
    """
    Save the generated data to a CSV file with columns named X1, X2, ...
    """
    n_cols = data.shape[1]
    col_names = [f'X{i+1}' for i in range(n_cols)]
    df = pd.DataFrame(data, columns=col_names)
    # Ensure output directory exists
    dir_name = os.path.dirname(filename)
    if dir_name != '':
        os.makedirs(dir_name, exist_ok=True)
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')

def save_dag(adj_matrix, filename='dag.csv'):
    """
    Save the DAG adjacency matrix to a CSV file with columns and index named X1, X2, ...
    """
    n = adj_matrix.shape[0]
    col_names = [f'X{i+1}' for i in range(n)]
    df = pd.DataFrame(adj_matrix, columns=col_names, index=col_names)
    # Ensure output directory exists
    dir_name = os.path.dirname(filename)
    if dir_name != '':
        os.makedirs(dir_name, exist_ok=True)
    df.to_csv(filename)
    print(f'DAG saved to {filename}')

def main(config_path='config.json'):
    # Load parameters from config file
    config = load_config(config_path)

    seed = config.get('seed', 18)
    n_nodes = config.get('n_nodes', 10)
    n_edges = config.get('n_edges', 17)
    n_samples = config.get('n_samples', 10000)
    method = config.get('method', 'linear')
    sem_type = config.get('sem_type', 'gauss')
    dag_type = config.get('dag_type', 'scale_free')  # 'scale_free' or 'custom'
    custom_adj = config.get('custom_adj', None)
    save_filename = config.get('save_filename', 'res/synthetic_dataset.csv')
    dag_save_filename = config.get('dag_save_filename', 'res/dag.csv')
    n_datasets = config.get('n_datasets', 10)

    # 保存先フォルダを分ける
    base_save_filename = os.path.join('res', 'dataset', os.path.basename(save_filename))
    base_dag_save_filename = os.path.join('res', 'dag_GT', os.path.basename(dag_save_filename))

    # 実行前に既存のCSVファイルをクリーンアップ
    dataset_pattern = base_save_filename.replace('.csv', '_seed*.csv')
    dag_pattern = base_dag_save_filename.replace('.csv', '_seed*.csv')

    for file_path in glob.glob(dataset_pattern):
        try:
            os.remove(file_path)
            print(f'Removed existing dataset file: {file_path}')
        except Exception as e:
            print(f'Error removing file {file_path}: {e}')

    for file_path in glob.glob(dag_pattern):
        try:
            os.remove(file_path)
            print(f'Removed existing DAG file: {file_path}')
        except Exception as e:
            print(f'Error removing file {file_path}: {e}')

    for i in range(n_datasets):
        current_seed = seed + i

        if dag_type == 'scale_free':
            dag = generate_scale_free_dag(n_nodes=n_nodes, n_edges=n_edges, seed=current_seed)
        elif dag_type == 'custom' and custom_adj is not None:
            dag = np.array(custom_adj)
        else:
            raise ValueError("Invalid DAG type or missing custom adjacency matrix.")

        # DAGの可視化は削除（表示しない）
        # if i == 0:
        #     visualize_dag(dag, title='DAG Visualization')

        data = simulate_data(dag, n_samples=n_samples, method=method, sem_type=sem_type)
        print(f'Data shape (seed={current_seed}): {data.shape}')

        current_save_filename = base_save_filename.replace('.csv', f'_seed{current_seed}.csv')
        current_dag_save_filename = base_dag_save_filename.replace('.csv', f'_seed{current_seed}.csv')

        save_data(data, filename=current_save_filename)
        save_dag(dag, filename=current_dag_save_filename)

if __name__ == '__main__':
    main()