import os
import glob
import shutil
from create_dataset import main

def create_dummy_files():
    os.makedirs('res/dataset', exist_ok=True)
    os.makedirs('res/dag_GT', exist_ok=True)
    # ダミーファイルを作成
    with open('res/dataset/synthetic_dataset_seed999.csv', 'w') as f:
        f.write('dummy data\n')
    with open('res/dag_GT/dag_seed999.csv', 'w') as f:
        f.write('dummy dag\n')

def check_files_exist(pattern):
    return len(glob.glob(pattern)) > 0

def test_cleanup():
    create_dummy_files()
    # ダミーファイルが存在することを確認
    assert check_files_exist('res/dataset/synthetic_dataset_seed999.csv'), "Dummy dataset file not created"
    assert check_files_exist('res/dag_GT/dag_seed999.csv'), "Dummy dag file not created"

    # main()を実行（config.jsonの設定に従う）
    main()

    # ダミーファイルが削除されていることを確認
    assert not check_files_exist('res/dataset/synthetic_dataset_seed999.csv'), "Dummy dataset file was not removed"
    assert not check_files_exist('res/dag_GT/dag_seed999.csv'), "Dummy dag file was not removed"

    print("Cleanup test passed.")

if __name__ == '__main__':
    test_cleanup()