import time
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray


class MAF3_Subscriber:
    def __init__(self):
        rospy.Subscriber("/ft_senser/ft_value", Float64MultiArray, self.callback_ft_value)
        self.ft_value                    = None
        self.connection_flag             = {}
        self.connection_flag["ft_value"] = False
        self.subscribe_sum               = len(self.connection_flag)
        self.wait_connection()


    def wait_connection(self):
        while not self.is_connection_established():
            time.sleep(0.3)
        print("---------------------------------------------------")
        print("  [connection is established]   MAF3_Subscriber    ")
        print("---------------------------------------------------")


    def is_connection_established(self):
        return np.sum(np.array(list(self.connection_flag.values()))*1) == self.subscribe_sum


    def callback_ft_value(self, data):
        self.ft_value = np.array(data.data)
        self.connection_flag["ft_value"] = True


if __name__ == '__main__':

    rospy.init_node("marker_node")
    sub = MAF3_Subscriber()


    for i in range(100):
        print("[{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}]".format(*sub.ft_value))
        time.sleep(0.1)
