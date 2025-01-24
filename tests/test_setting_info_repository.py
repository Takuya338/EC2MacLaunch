import unittest
from infrastructure.setting_info_repository import SettingInfoRepository

class TestSettingInfoRepository(unittest.TestCase):
    def setUp(self):
        """テストの前準備"""
        self.repository = SettingInfoRepository()

    def test_load_file(self):
        """実際のファイルを読み込むテスト"""
        result = self.repository.load()
        self.assertEqual(result, ['region-code:ap-northeast-1', 'instance ID:i-0da88385dc93c45ac'])

    def test_file_name(self):
        self.assertEqual(self.repository.FILE_NAME, 'setting.config')

if __name__ == '__main__':
    unittest.main()
