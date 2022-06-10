from email import header
from mimetypes import init
from black import main
from matplotlib.pyplot import pink
from numpy import piecewise
import rospy
from std_msgs.msg import Float64MultiArray
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Vector3
from std_msgs.msg import ColorRGBA

from MAF3_SerialCommunication import MAF3_SerialCommunication
from MAF3_MarkerArray import MAF3_MarkerArray


class MAF3_RVIZ:
    def __init__(self):
        self.ft_ser          = MAF3_SerialCommunication(port_name="/dev/ttyUSB0")
        self.ft_marker_array = MAF3_MarkerArray()


    def main(self):

        rospy.init_node("marker_array_node")

        marker_array_pub = rospy.Publisher("marker_array", MarkerArray, queue_size = 100)
        ft_pub = rospy.Publisher("/ft_senser/ft_value", Float64MultiArray, queue_size = 100)

        rate = rospy.Rate(60)

        self.ft_ser.open()
        while not rospy.is_shutdown():

            weight = self.ft_ser._read_all_weight()
            marker_array_msg = self.ft_marker_array.create(weight)
            marker_array_pub.publish(marker_array_msg)

            ft_msg = Float64MultiArray()
            ft_msg.data = self.ft_ser.read_weight()
            ft_pub.publish(ft_msg)

            self.ft_ser.print_weight(weight)

            # print(self.ft_marker_array.position.y)
            rate.sleep()


if __name__ == '__main__':
    rviz = MAF3_RVIZ()

    try:
        rviz.main()
        rviz.ft_ser.close()
    finally:
        rviz.ft_ser.close()
        print("close!")

