import pandas as pd
from castle.metrics import MetricsDAG

def evaluate_dag_estimation(causal_matrix, true_dag):
    """
    DirectLiNGAMの推定結果と真のDAGを比較し、評価指標を計算して辞書で返す関数。
    他のプログラムでも利用可能。
    """
    metrics = MetricsDAG(causal_matrix, true_dag)
    print("\nEvaluation Metrics:")
    print(f"DirectLiNGAM SHD: {metrics.metrics['shd']}")
    print(f"DirectLiNGAM F1 Score: {metrics.metrics['F1']}")
    return {
        'shd': metrics.metrics['shd'],
        'F1': metrics.metrics['F1']
    }