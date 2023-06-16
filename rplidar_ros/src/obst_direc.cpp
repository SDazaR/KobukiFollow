#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/Joy.h>
#include <kobuki_msgs/MotorPower.h>
#include <kobuki_msgs/KeyboardInput.h> // keycodes from remote teleops.

class ObstDirec{
public: 
ObstDirec;

private:

  ros::NodeHandle nh_;

  ros::Publisher vel_pub_;
  ros::Subscriber scan_sub_;
};


ObstDirec::ObstDirec():
{
  vel_pub_ = nh_.advertise<geometry_msgs::Twist>("/mobile_base/commands/velocity", 1);
  scan_sub_ = nh_.subscribe<sensor_msgs::Joy>("scan",360, &TeleopTurtle::joyCallback, this);
}


