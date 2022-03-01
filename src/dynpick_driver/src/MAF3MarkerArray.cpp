#include "MAF3MarkerArray.hpp"
#include <stdio.h>
#include <string>
#include <termios.h>
#include <geometry_msgs/WrenchStamped.h>
#include <visualization_msgs/MarkerArray.h>


std::string header_frame_id  = "world";
std::string header_namespace = "cmd_vel_display";
double moment_arrow_offset   = 0.3;

double x = 0.0;
double y = 0.0;
double z = 0.0;

#define SCALE_ARROW_FORCE  0.2
#define SCALE_ARROW_MOMENT 0.4

#define COLOR_FZ_R 0.0
#define COLOR_FZ_G 1.0
#define COLOR_FZ_B 0.0
#define COLOR_FZ_A 1.0

#define COLOR_MX_R 1.0
#define COLOR_MX_G 0.0
#define COLOR_MX_B 0.0
#define COLOR_MX_A 1.0

#define COLOR_MY_R 0.0
#define COLOR_MY_G 0.0
#define COLOR_MY_B 1.0
#define COLOR_MY_A 1.0

#define ORIENTATION_X 0.0
#define ORIENTATION_Y 0.0
#define ORIENTATION_Z 0.0
#define ORIENTATION_W 1.0



void MAF3MarkerArray::set_marker_Fz(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end){
    (*marker).header.frame_id    = header_frame_id;
    (*marker).header.stamp       = ros::Time::now();
    (*marker).ns                 = header_namespace;
    (*marker).id                 = 0;
    (*marker).lifetime           = ros::Duration();

    (*marker).type               = visualization_msgs::Marker::ARROW;
    (*marker).action             = visualization_msgs::Marker::ADD;
    (*marker).scale              = arrow;

    (*marker).points.resize(2);
    (*marker).points[0]          = arrow_start;
    (*marker).points[1]          = arrow_end;

    (*marker).color.r            = COLOR_FZ_R;
    (*marker).color.g            = COLOR_FZ_G;
    (*marker).color.b            = COLOR_FZ_B;
    (*marker).color.a            = COLOR_FZ_A;

    (*marker).pose.orientation.x = ORIENTATION_X;
    (*marker).pose.orientation.y = ORIENTATION_Y;
    (*marker).pose.orientation.z = ORIENTATION_Z;
    (*marker).pose.orientation.w = ORIENTATION_W;
}


void MAF3MarkerArray::set_marker_Mx(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end){
    (*marker).header.frame_id    = header_frame_id;
    (*marker).header.stamp       = ros::Time::now();
    (*marker).ns                 = header_namespace;
    (*marker).id                 = 1;
    (*marker).lifetime           = ros::Duration();

    (*marker).type               = visualization_msgs::Marker::ARROW;
    (*marker).action             = visualization_msgs::Marker::ADD;
    (*marker).scale              = arrow;

    (*marker).points.resize(2);
    (*marker).points[0]          = arrow_start;
    (*marker).points[1]          = arrow_end;

    (*marker).color.r            = COLOR_MX_R;
    (*marker).color.g            = COLOR_MX_G;
    (*marker).color.b            = COLOR_MX_B;
    (*marker).color.a            = COLOR_MX_A;

    (*marker).pose.orientation.x = ORIENTATION_X;
    (*marker).pose.orientation.y = ORIENTATION_Y;
    (*marker).pose.orientation.z = ORIENTATION_Z;
    (*marker).pose.orientation.w = ORIENTATION_W;
}


void MAF3MarkerArray::set_marker_My(visualization_msgs::Marker *marker, geometry_msgs::Vector3 arrow, geometry_msgs::Point arrow_start, geometry_msgs::Point arrow_end){
    (*marker).header.frame_id    = header_frame_id;
    (*marker).header.stamp       = ros::Time::now();
    (*marker).ns                 = header_namespace;
    (*marker).id                 = 2;
    (*marker).lifetime           = ros::Duration();

    (*marker).type               = visualization_msgs::Marker::ARROW;
    (*marker).action             = visualization_msgs::Marker::ADD;
    (*marker).scale              = arrow;

    (*marker).points.resize(2);
    (*marker).points[0]          = arrow_start;
    (*marker).points[1]          = arrow_end;

    (*marker).color.r            = COLOR_MY_R;
    (*marker).color.g            = COLOR_MY_G;
    (*marker).color.b            = COLOR_MY_B;
    (*marker).color.a            = COLOR_MY_A;

    (*marker).pose.orientation.x = ORIENTATION_X;
    (*marker).pose.orientation.y = ORIENTATION_Y;
    (*marker).pose.orientation.z = ORIENTATION_Z;
    (*marker).pose.orientation.w = ORIENTATION_W;
}


// void set_marker_My_positive();
// void set_marker_My_negative();



// void set_marker(double *weight, string header_frame_id, uint64_t header_stamp){

// }

int MAF3MarkerArray::sign(double A){
    return (A>0)-(A<0);
}

// --------------------------
//      weight[0] : Fx
//      weight[1] : Fy
//      weight[2] : Fz
//      weight[3] : Mx
//      weight[4] : My
//      weight[5] : Mz
// --------------------------

visualization_msgs::MarkerArray  MAF3MarkerArray::get_marker_array(double *weight){

    visualization_msgs::MarkerArray marker_array;
    marker_array.markers.resize(3);

    geometry_msgs::Vector3 arrow;  // config arrow shape
    arrow.x = 0.02;
    arrow.y = 0.04;
    arrow.z = 0.1;

    // =============================
    //              Fz
    // =============================
    geometry_msgs::Point arrow_start;
    arrow_start.x = 0.0;
    arrow_start.y = 0.0;
    arrow_start.z = 0.0;

    geometry_msgs::Point arrow_end;
    arrow_end.x   = 0.0;
    arrow_end.y   = 0.0;
    arrow_end.z   = weight[2] * SCALE_ARROW_FORCE;

    set_marker_Fz(&marker_array.markers[0], arrow, arrow_start, arrow_end);


    // =============================
    //              Mx
    // =============================
    arrow_end.x   = 0.0;
    arrow_end.y   = weight[3] * SCALE_ARROW_MOMENT;
    arrow_end.z   = 0.0;
    set_marker_Mx(&marker_array.markers[1], arrow, arrow_start, arrow_end);


    // =============================
    //              My
    // =============================
    arrow_end.x   = -weight[4] * SCALE_ARROW_MOMENT;
    arrow_end.y   = 0.0;
    arrow_end.z   = 0.0;
    set_marker_My(&marker_array.markers[2], arrow, arrow_start, arrow_end);


    return marker_array;
}