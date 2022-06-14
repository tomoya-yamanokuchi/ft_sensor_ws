import signal
from multiprocessing.context import ForkContext
from time import time
from black import main
import numpy as np
import rospy

from std_msgs.msg import Float64MultiArray
import os

import sys
ft_sensor_ws = "/home/tomoya-y/ft_sensor_ws/src/dynpick_driver/src"
sys.path.append(ft_sensor_ws)
from MAF3_Subscriber import MAF3_Subscriber
import pathlib



class CalibrationFTSensor:
    def __init__(self):
        rospy.init_node("MAF3_node")
        self.ft_sub    = MAF3_Subscriber()
        p              = pathlib.Path(__file__)
        self.save_path = "/".join(str(p.parent).split("/")[:-1]) + "/calibration_data"
        os.makedirs(self.save_path, exist_ok=True)


    def measure_ft_bias(self, num_measure=100, rate=30, idx=1):
        bias = np.random.randn(num_measure, 3)
        rate = rospy.Rate(rate)
        for i in range(num_measure):
            bias[i] = self.ft_sub.ft_value
            print("{:3d}/{:3d}: [{: .3f}, {: .3f}, {: .3f}]".format(i, num_measure, bias[i, 0], bias[i, 1], bias[i, 2]))
            rate.sleep()
        np.save(self.save_path + "/bias_mean_idx{}.npy".format(idx), np.mean(bias, axis=0))
        np.save(self.save_path +  "/bias_std_idx{}.npy".format(idx),   np.std(bias, axis=0))
        print("*** finished ***")


    def run(self):
        self.measure_ft_bias(num_measure=500, rate=30, idx=1)


if __name__ == '__main__':

        try:
            test = CalibrationFTSensor()
            test.run()
        except KeyboardInterrupt:
            sys.exit()


