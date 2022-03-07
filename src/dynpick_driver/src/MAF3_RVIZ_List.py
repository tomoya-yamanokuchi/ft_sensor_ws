from email import header
from mimetypes import init
from black import main
from matplotlib.pyplot import pink
import rospy
import numpy as np
from visualization_msgs.msg import Marker, MarkerArray
from MAF3_SerialCommunicationList import MAF3_SerialCommunicationList
from MAF3_MarkerArrayList import MAF3_MarkerArrayList
import serial.tools.list_ports
from omegaconf import OmegaConf



class MAF3_RVIZ_List:
    def __init__(self):
        self.serial_number_config       = OmegaConf.load("src/dynpick_driver/src/MAF3_serial_number.yaml")
        serial_number_in_order          = [self.serial_number_config[key] for key in list(np.sort(list(self.serial_number_config.keys())))]
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
        self.ft_marker_array_list = MAF3_MarkerArrayList(
            namespace_list             = ["ft{}".format(n) for n in range(self.n_sensor)],
            arrow_position_offset_list = [[0.0, -1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
        )


    def main(self):
        rospy.init_node("marker_array_node")

        marker_array_pub = rospy.Publisher("marker_array", MarkerArray, queue_size = 100)
        rate = rospy.Rate(60)

        self.ft_ser_list.open()
        while not rospy.is_shutdown():
            weight_list = self.ft_ser_list.read_weight()
            marker_array_msg = self.ft_marker_array_list.create(weight_list)
            marker_array_pub.publish(marker_array_msg)
            self.ft_ser_list.print_weight(weight_list)
            rate.sleep()



if __name__ == '__main__':
    rviz = MAF3_RVIZ_List()

    try:
        rviz.main()
        rviz.ft_ser_list.close()
    finally:
        rviz.ft_ser_list.close()
        print("close!")

