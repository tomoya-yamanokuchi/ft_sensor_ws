from email import header
from mimetypes import init
from black import main
from matplotlib.pyplot import pink
import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Vector3
from std_msgs.msg import ColorRGBA

from MAF3_SerialCommunication import MAF3_SerialCommunication
from MAF3_MarkerArray import MAF3_MarkerArray


class MAF3_RVIZ:
    def __init__(self):
        self.ft_ser          = MAF3_SerialCommunication()
        self.ft_marker_array = MAF3_MarkerArray()


    def main(self):


        rospy.init_node("marker_array_node")

        marker_array_pub = rospy.Publisher("marker_array", MarkerArray, queue_size = 100)
        rate = rospy.Rate(30)


        self.ft_ser.open()
        while not rospy.is_shutdown():

            weight = self.ft_ser.read_weight()
            marker_array_msg = self.ft_marker_array.create(weight)
            marker_array_pub.publish(marker_array_msg)

            self.ft_ser.print_weight(weight)
            rate.sleep()



if __name__ == '__main__':
    rviz = MAF3_RVIZ()

    try:
        rviz.main()
        rviz.ft_ser.close()
    finally:
        rviz.ft_ser.close()
        print("close!")
