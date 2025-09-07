import os
import unittest
import pandas as pd
from lingam_example import main

class TestLingamExample(unittest.TestCase):
    def test_main_creates_predicted_dag_csv(self):
        # 実行
        main()

        # 期待されるファイルパス
        expected_path = os.path.join('res', 'pred_dag_synthetic_dataset.csv')

        # ファイルが存在すること
        self.assertTrue(os.path.exists(expected_path), f"{expected_path} が存在しません。")

        # ファイルサイズが0でないこと
        self.assertGreater(os.path.getsize(expected_path), 0, f"{expected_path} が空ファイルです。")

        # ファイルの中身が正しいか簡単に確認（ヘッダーにX1が含まれているか）
        df = pd.read_csv(expected_path, index_col=0)
        self.assertIn('X1', df.columns)
        self.assertIn('X1', df.index)

if __name__ == '__main__':
    unittest.main()