import os
import unittest
import pandas as pd
from lingam_example import main

class TestLingamExample(unittest.TestCase):
    def test_main_creates_predicted_dag_csv(self):
        import glob
        # 実行
        main()

        pred_dir = 'res/predicted_dags'
        pred_files = glob.glob(os.path.join(pred_dir, 'pred_dag_synthetic_dataset_seed*.csv'))
        self.assertGreater(len(pred_files), 0, f"{pred_dir} に推論結果ファイルがありません。")

        for expected_path in pred_files:
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