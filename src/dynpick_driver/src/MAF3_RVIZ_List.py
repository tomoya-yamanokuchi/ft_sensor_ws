from email import header
from importlib.resources import path
from mimetypes import init
from black import main
from matplotlib.pyplot import pink
import rospy
import numpy as np
from std_msgs.msg import Int16MultiArray, Float64MultiArray
from visualization_msgs.msg import Marker, MarkerArray
from MAF3_SerialCommunicationList import MAF3_SerialCommunicationList
from MAF3_MarkerArrayList import MAF3_MarkerArrayList
import serial.tools.list_ports
from omegaconf import OmegaConf

import pathlib

class MAF3_RVIZ_List:
    def __init__(self):
        p                               = pathlib.Path(__file__)
        self.serial_number_config       = OmegaConf.load(str(p.parent) + "/MAF3_serial_number.yaml")
        # serial_number_in_order          = [self.serial_number_config[key] for key in list(np.sort(list(self.serial_number_config.keys())))]
        serial_number_in_order          = [self.serial_number_config[key] for key in list(self.serial_number_config.keys())]
        ports                           = list(serial.tools.list_ports.comports())
        usb_port_and_serial_number_dict = {}
        for p in ports:
            if "USB" in p.device:
                usb_port_and_serial_number_dict[p.serial_number] = p.device
                print("p.serial_number", p.serial_number)

        self.n_sensor             = len(list(usb_port_and_serial_number_dict.keys()))
        self.ft_ser_list          = MAF3_SerialCommunicationList(
            port_name_list = [usb_port_and_serial_number_dict[serial_number_in_order_i] for serial_number_in_order_i in serial_number_in_order]
        )
        offset = 0.5
        self.ft_marker_array_list = MAF3_MarkerArrayList(
            namespace_list             = ["ft{}".format(n) for n in range(self.n_sensor)],
            # arrow_position_offset_list = [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 20.0, 0.0]]
            arrow_position_offset_list = [[offset, offset, 0.0], [-offset, -offset, 0.0], [0.0, 20.0, 0.0]]
        )
        self.load_calib_data()


    def load_calib_data(self):
        p              = pathlib.Path()
        save_path      = "/".join(str(p.cwd()).split("/")[:-1]) + "/ft_sensor_ws/src/dynpick_driver/calibration_data"
        self.bias_mean = [0]*self.n_sensor
        self.bias_std  = [0]*self.n_sensor
        for i in range(self.n_sensor):
            self.bias_mean[i] = np.load(save_path + "/bias_mean_idx{}.npy".format(i))
            self.bias_std [i] = np.load(save_path +  "/bias_std_idx{}.npy".format(i))


    def get_force_status(self, ft_value, bias_mean, bias_std):
        force = [None] * 3
        for i in range(3):
            lb  = bias_mean[i] - 4 * bias_std[i]
            ub  = bias_mean[i] + 4 * bias_std[i]
            val = ft_value[i]
            if   lb <= val < ub : force[i] = 0
            else                : force[i] = 1
        return force


    def get_force_status_collection(self, ft_value_collection):
        assert type(ft_value_collection) is list
        return [self.get_force_status(ft_value_collection[i], self.bias_mean[i], self.bias_std[i]) for i in range(self.n_sensor)]



    def main(self):
        rospy.init_node("MAF3_publish_node")
        marker_array_pub = rospy.Publisher("/ft_sensor/marker_array",   MarkerArray,        queue_size = 100)
        ft_raw_pub       = rospy.Publisher("/ft_sensor/ft_raw_value",   Float64MultiArray,  queue_size = 100)
        ftg_status_pub   = rospy.Publisher("/ft_sensor/ft_status",      Int16MultiArray,    queue_size = 100)
        rate             = rospy.Rate(240)

        self.ft_ser_list.open()
        while not rospy.is_shutdown():
            weight_list = self.ft_ser_list.read_weight(is_hstack=False)

            # '''
            #     marker
            # '''
            # marker_array_msg = self.ft_marker_array_list.create(weight_list)
            # marker_array_pub.publish(marker_array_msg)
            # self.ft_ser_list.print_weight(weight_list)

            '''
                ft_raw_value
            '''
            ft_msg      = Float64MultiArray()
            ft_msg.data = np.hstack(weight_list) # self.ft_ser_list.read_weight()
            ft_raw_pub.publish(ft_msg)

            # '''
            #     force_status
            # '''
            # ft_status_msg      = Int16MultiArray()
            # ft_status_msg.data = np.hstack(self.get_force_status_collection(weight_list))
            # ftg_status_pub.publish(ft_status_msg)

            rate.sleep()
            # time.sleep()


if __name__ == '__main__':
    rviz = MAF3_RVIZ_List()

    try:
        rviz.main()
        rviz.ft_ser_list.close()
    finally:
        rviz.ft_ser_list.close()
        print("close!")

