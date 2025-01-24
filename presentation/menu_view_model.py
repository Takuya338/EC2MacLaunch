from utils.ec2_status import EC2Status

class MenuViewModel():
    def __init__(self, ec2_instane, current_ec2_status):
        self.current_ec2_status = current_ec2_status

    def get_result_message(self):
        return "テスト中です。"
    
    def get_ec2_status(self):
        if self.current_ec2_status == EC2Status.RUNNING:
            return EC2Status.STOPPING
        else:
            return EC2Status.RUNNING
        