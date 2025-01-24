from presentation.menu_view import MenuView
from application.ec2_service import EC2Service
from presentation.menu_view_model import MenuViewModel 

def main():
    # サービスクラス
    ec2_service_instance = EC2Service()

    # 起動画面を開く
    app = MenuView(ec2_service_instance)
    app.mainloop()

if __name__ == "__main__":
    main()