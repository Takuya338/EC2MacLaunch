import unittest
from unittest.mock import Mock, patch
from tkinter import messagebox
from presentation.menu_view import MenuView
from utils.ec2_status import EC2Status

class TestMenuView(unittest.TestCase):
    def setUp(self):
        # EC2Serviceのモックを作成
        self.mock_ec2_service = Mock()
        # MenuViewのインスタンスを作成
        self.menu_view = MenuView(self.mock_ec2_service)

    def test_initialize_window(self):
        """ウィンドウの初期設定が正しく行われることを確認"""
        self.assertEqual(self.menu_view.title(), "EC2Launch")
        self.menu_view.update()  # ウィンドウの更新を強制
        geometry = self.menu_view.winfo_geometry()
        width = self.menu_view.winfo_width()
        height = self.menu_view.winfo_height()
        self.assertEqual(width, 250)
        self.assertEqual(height, 120)
        self.assertFalse(self.menu_view.resizable()[0])
        self.assertFalse(self.menu_view.resizable()[1])

    def test_get_button_name(self):
        """ボタン名が正しく設定されることを確認"""
        self.assertEqual(self.menu_view.get_button_name(EC2Status.STOPPING), "起動")
        self.assertEqual(self.menu_view.get_button_name(EC2Status.RUNNING), "停止")

    @patch('tkinter.messagebox.showinfo')
    def test_on_click_boot_button_when_stopping(self, mock_showinfo):
        """EC2が停止状態の時の起動ボタン押下処理を確認"""
        # モックの設定
        mock_showinfo.return_value = 'ok'
        self.menu_view.ec2_status = EC2Status.STOPPING
        mock_instance = Mock()
        self.mock_ec2_service.start_ec2.return_value = mock_instance

        # テスト実行
        self.menu_view.on_click_boot_button()

        # 検証
        self.mock_ec2_service.start_ec2.assert_called_once()
        mock_showinfo.assert_called_once()
        self.assertEqual(self.menu_view.launch_button['state'], 'normal')

    @patch('tkinter.messagebox.showinfo')
    def test_on_click_boot_button_when_running(self, mock_showinfo):
        """EC2が起動状態の時の停止ボタン押下処理を確認"""
        # モックの設定
        mock_showinfo.return_value = 'ok'
        self.menu_view.ec2_status = EC2Status.RUNNING
        mock_instance = Mock()
        self.mock_ec2_service.stop_ec2.return_value = mock_instance

        # テスト実行
        self.menu_view.on_click_boot_button()

        # 検証
        self.mock_ec2_service.stop_ec2.assert_called_once()
        mock_showinfo.assert_called_once()
        self.assertEqual(self.menu_view.launch_button['state'], 'normal')

    def test_do_action_to_ec2_instance(self):
        """EC2インスタンスに対する処理が正しく実行されることを確認"""
        # 起動処理のテスト
        self.menu_view.do_action_to_ec2_instance(EC2Status.STOPPING)
        self.mock_ec2_service.start_ec2.assert_called_once()

        # 停止処理のテスト
        self.menu_view.do_action_to_ec2_instance(EC2Status.RUNNING)
        self.mock_ec2_service.stop_ec2.assert_called_once()

if __name__ == '__main__':
    unittest.main() 