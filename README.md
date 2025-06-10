
# URDF Basic

The project illustrates how to write a URDF file and how to run it using RViz




## Setup

For project we need to setup ROS2. Here we will be using ROS2 Jazzy.
To install and setup ROS2 Jazzy Follow the https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html to install ROS2 Jazzy (follow step-by-step) 
Note: do NOT run the command 
```bash
 sudo apt install ros-jazzy-ros-base  
 ``` 
in the Install ROS2 section.

RViz should also be installed. To install rviz run in the terminal 
```bash 
sudo apt install ros-jazzy-rviz2
```




    
## Usage

After saving the urdf file code you will need to create a launch file as given. 

After that inside the terminal run 
```bash
ros2 launch ~/{your launch file location}
```
Use the slidebars to see movement of every joint.

