#include <ros/ros.h>
#include <string>
#include <math.h>

#include <MAF3_msgs/MAF3_Raw.h>



int main(int argc, char** argv){

  ros::init(argc, argv, "pseudo_force_torque_publisher");
  ros::NodeHandle nh;

  // publisher
  ros::Publisher maf3_pub = nh.advertise<MAF3_msgs::MAF3_Raw>("MAF3_Raw", 1);

  ros::Rate loop_rate(30);
  while (ros::ok()){
    MAF3_msgs::MAF3_Raw maf3_msg;
    // maf3_msg.header.frame_id = "world";
    // maf3_msg.header.stamp    = ros::Time::now();


        // char key;

        // cin >> key;
        // cout << key << endl; // 読み込んだキーの値を標準出力へ出力

        // switch (key) {
        //   case 'z':
        //       maf3_msg.Fz  =  22;
        //       break;
        //   case 'x':
        //       maf3_msg.Mx  =  12;
        //       break;
        //   case 'y':
        //       maf3_msg.My  =  5;
        //       break;
        // }

    // maf3_msg.Fz = 10;
    // maf3_msg.Mx = 2;
    // maf3_msg.My = 2;

    maf3_pub.publish(maf3_msg);

    maf3_msg.Fz = 0;
    maf3_msg.Mx = 0;
    maf3_msg.My = 0;

    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}