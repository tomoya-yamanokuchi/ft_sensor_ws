import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Vector3
from std_msgs.msg import ColorRGBA
from RGBA import RGBA
from MAF3_MarkerArray import MAF3_MarkerArray


class MAF3_MarkerArrayList:
    def __init__(self, namespace_list, arrow_position_offset_list):
        self.n_sensor     = len(arrow_position_offset_list)
        self.marker_array = [MAF3_MarkerArray(namespace_list[i], arrow_position_offset_list[i]) for i in range(self.n_sensor)]


    def create(self, weight_list):
        marker_array_msg = MarkerArray()
        for i in range(self.n_sensor):
            marker_array_msg = self.marker_array[i].create(weight_list[i], marker_array_msg)
        return marker_array_msg