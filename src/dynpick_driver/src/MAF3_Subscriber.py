import time
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray, Int16MultiArray


class MAF3_Subscriber:
    def __init__(self):
        rospy.Subscriber("/ft_sensor/ft_raw_value", Float64MultiArray, self.callback_ft_raw_value)
        rospy.Subscriber("/ft_sensor/ft_status",    Int16MultiArray,   self.callback_ft_status)
        self.ft_raw_value                    = None
        self.ft_status                       = None
        self.connection_flag                 = {}
        self.connection_flag["ft_raw_value"] = False
        self.connection_flag["ft_status"]    = False
        self.subscribe_sum                   = len(self.connection_flag)
        self.wait_connection()


    def wait_connection(self):
        while not self.is_connection_established():
            time.sleep(0.3)
        rospy.loginfo("MAF3_Subscriber is established!")


    def is_connection_established(self):
        return np.sum(np.array(list(self.connection_flag.values()))*1) == self.subscribe_sum


    def callback_ft_raw_value(self, data):
        self.ft_raw_value = np.array(data.data)
        self.connection_flag["ft_raw_value"] = True


    def callback_ft_status(self, data):
        self.ft_status = np.array(data.data)
        self.connection_flag["ft_status"] = True


if __name__ == '__main__':

    rospy.init_node("marker_node")
    sub = MAF3_Subscriber()

    for i in range(1000):
        # print("[{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}] [{: .2f}, {: .2f}, {: .2f}]".format(*sub.ft_raw_value))
        print("[{: 1d}, {: 1d}, {: 1d}] [{: 1d}, {: 1d}, {: 1d}] [{: 1d}, {: 1d}, {: 1d}]".format(*sub.ft_status))
        time.sleep(0.1)
