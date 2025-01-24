import os

"""設定情報読み込みクラス"""
class SettingInfoRepository():
    # ファイル名
    FILE_NAME = 'setting.config'

    """設定ファイルを読み込み、行ごとの配列を返す"""
    """@return list: 設定ファイルの各行を要素とする配列"""
    def load(self):
     file_array = []
     try:
            file_path = os.path.join(os.path.dirname(__file__), self.FILE_NAME)  # スクリプトと同じ場所にあるファイル
            with open(file_path, encoding="utf-8") as file:
                for line in file:
                    file_array.append(line.strip())  # 各行をリストに追加
            return file_array
     except FileNotFoundError:
            print(f"Error: File '{self.FILE_NAME}' not found.")
            return []
        