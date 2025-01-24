from enum import Enum

class EC2Status(Enum):
    STOPPING = 0  # 停止中
    RUNNING =1    # 起動中