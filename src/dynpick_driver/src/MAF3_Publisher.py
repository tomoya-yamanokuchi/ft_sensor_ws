import rospy
from std_msgs.msg import Float64MultiArray
from MAF3_SerialCommunication import MAF3_SerialCommunication


class MAF3_Publisher:
    def run(self):
        rospy.init_node("ft_sensor_node")
        self.ft_ser = MAF3_SerialCommunication(port_name="/dev/ttyUSB0")
        ft_pub      = rospy.Publisher("/ft_senser/ft_value", Float64MultiArray, queue_size = 100)
        rate        = rospy.Rate(60)

        self.ft_ser.open()
        while not rospy.is_shutdown():
            ft_msg      = Float64MultiArray()
            ft_msg.data = self.ft_ser.read_weight()
            ft_pub.publish(ft_msg)
            print("{: .3f}, {: .3f}, {: .3f}".format(*ft_msg.data))
            rate.sleep()


if __name__ == '__main__':
    pub = MAF3_Publisher()

    try:
        pub.run()
        pub.ft_ser.close()
    finally:
        pub.ft_ser.close()
        print("close!")

