11/21 simulation environment

Ubuntu 24.04

ROS 2 Jazzy

Packages:

navigation2

nav2_bringup

slam_toolbox

robot_localization

ros2_control

ros2_controllers

xacro

behaviortree_cpp

ros_gz


Build:

source /opt/ros/jazzy/setup.bash

colcon build


Run:シミュレーター起動

ros2 launch my_robot_sim sim_nav2.launch.py


簡単にセットアップ \
sudo apt update \

sudo apt install -y \
ros-jazzy-desktop \
ros-jazzy-navigation2 \
ros-jazzy-nav2-bringup \
ros-jazzy-slam-toolbox \
ros-jazzy-robot-localization \
ros-jazzy-ros2-control \
ros-jazzy-ros2-controllers \
ros-jazzy-behaviortree-cpp \
ros-jazzy-ros-gz \
ros-jazzy-xacro \
python3-colcon-common-extensions \
python3-rosdep \

rosdep install \
--from-paths src \
--ignore-src \
-r -y \
