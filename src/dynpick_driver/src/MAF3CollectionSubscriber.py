import time
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray
from MAF3_Subscriber import MAF3_Subscriber

class MAF3CollectionSubscriber(MAF3_Subscriber):
    def __init__(self):
        super().__init__()

    @property
    def ft_raw_value_collection(self):
        return np.split(self.ft_raw_value, 3)


    @property
    def ft_status_collection(self):
        return np.split(self.ft_status, 3)


if __name__ == '__main__':

    rospy.init_node("marker_node")
    sub = MAF3CollectionSubscriber()

    for i in range(100):
        # print("[{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}]".format(*sub.ft_value))
        # print(sub.ft_raw_value_collection)
        print(sub.ft_status_collection)
        time.sleep(0.1)
