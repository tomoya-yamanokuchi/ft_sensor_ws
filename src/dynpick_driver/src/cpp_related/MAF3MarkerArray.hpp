#pragma once

#include <geometry_msgs/WrenchStamped.h>
#include <visualization_msgs/MarkerArray.h>

class MAF3MarkerArray{
    public:
        void set_marker_Fz(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end);
        void set_marker_Mx(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end);
        void set_marker_My(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end);
        int sign(double A);
        visualization_msgs::MarkerArray get_marker_array(double *weight);
};