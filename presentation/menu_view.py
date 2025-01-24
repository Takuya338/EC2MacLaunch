import tkinter as tk
from tkinter import messagebox
from application.ec2_service import EC2Service
from presentation.menu_view_model import MenuViewModel
from utils.ec2_status import EC2Status

"""管理画面"""
class MenuView(tk.Tk):
    """コンストラクタ"""
    def __init__(self, ec2_service_instance, master=None):
        super().__init__(master)
        self.master = master
        # EC2インスタンスの起動状態
        self.ec2_status = EC2Status.STOPPING
        # サービスクラス
        self.ec2_service_instance = ec2_service_instance
        # ウィンドウの初期化
        self.initialize_window()
        # ボタン作成と配置
        self.create_buttons()       

    """ウィンドウの初期設定を行うメソッド"""
    def initialize_window(self):        
        self.title("EC2Launch")
        self.geometry("250x120")
        self.resizable(False, False)

    """ボタンを作成し配置するメソッド"""
    def create_buttons(self):      
        self.launch_button = tk.Button(self, text=self.get_button_name(EC2Status.STOPPING), command=self.on_click_boot_button)
        self.launch_button.place(x=10, y=10, width=230, height=100)

    """起動ボタン押下時の処理を行うメソッド"""
    def on_click_boot_button(self):
        # ボタンを非活性化
        self.launch_button['state'] = 'disabled'

        # EC2インスタンスの起動または停止処理
        ec2_instance = self.do_action_to_ec2_instance(self.ec2_status)

        # 処理結果を表示用に変換
        menu_view_model = MenuViewModel(ec2_instance, self.ec2_status)

        # EC2の起動状態を更新
        self.ec2_status = menu_view_model.get_ec2_status()

        # OKアラートを表示
        result = tk.messagebox.showinfo("EC2Launch", menu_view_model.get_result_message())
        
        # OKボタン押下後の処理
        if result == 'ok':
            self.launch_button['text'] = self.get_button_name(menu_view_model.get_ec2_status())
            self.launch_button['state'] = 'normal'
    
    """ボタン名を設定するメソッド"""
    """@param status EC2の状態"""
    """@return ボタン名"""
    def get_button_name(self, ec2_status):
        if ec2_status == EC2Status.STOPPING:
            return "起動"
        else:
            return "停止"
    
    """EC2インスタンスに対して処理を行うメソッド"""
    """@param status EC2の状態"""
    """@return EC2インスタンス"""
    def do_action_to_ec2_instance(self, ec2_status):
        if ec2_status == EC2Status.STOPPING:
            # 起動処理
            return self.ec2_service_instance.start_ec2()
        else:
            # 停止処理
            return self.ec2_service_instance.stop_ec2()
        



