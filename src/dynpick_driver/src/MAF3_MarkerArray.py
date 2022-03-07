import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Vector3
from std_msgs.msg import ColorRGBA



class MAF3_MarkerArray:
    def __init__(self):
        self.frame_id    = "world"
        self.namespace   = "cmd_vel_display"
        self.arrow_scale = Vector3(x=0.02, y=0.04, z=0.1)
        self.position    = Point(x=0.0, y=0.0, z=0.0)
        self.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        self.n_axis      = 6 # MAF-3の軸数（Fz, Mx, My）
        self.red         = [1.0, 0.0, 0.0, 1.0]
        self.green       = [0.0, 1.0, 0.0, 1.0]
        self.blue        = [0.0, 0.0, 1.0, 1.0]


    def create_marker(self, id, xyz, rgba):
        marker                  = Marker()
        marker.header.frame_id  = self.frame_id
        marker.header.stamp     = rospy.Time.now()
        marker.ns               = self.namespace
        marker.id               = id
        marker.lifetime         = rospy.Duration()
        marker.type             = Marker.ARROW
        marker.action           = Marker.ADD
        marker.color            = ColorRGBA(r=rgba[0], g=rgba[1], b=rgba[2], a=rgba[3])
        marker.scale            = self.arrow_scale
        marker.pose.position    = self.position
        marker.pose.orientation = self.orientation
        marker.points.append(self.position)
        marker.points.append(Point(x=xyz[0], y=xyz[1], z=xyz[2]))
        return marker


    def create(self, weight):
        assert len(weight) == self.n_axis
        marker_array = MarkerArray()
        marker_array.markers.append(self.create_marker(id=0, xyz=[0.0, 0.0, weight[2]], rgba=[1.0, 0.0, 0.0, 1.0]))
        marker_array.markers.append(self.create_marker(id=1, xyz=[0.0, weight[2], 0.0], rgba=[0.0, 1.0, 0.0, 1.0]))
        marker_array.markers.append(self.create_marker(id=2, xyz=[weight[2], 0.0, 0.0], rgba=[0.0, 0.0, 1.0, 1.0]))
        return marker_array