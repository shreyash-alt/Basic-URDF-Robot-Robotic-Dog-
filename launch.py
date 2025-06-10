from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open('{your URDF file path}').read()}]
        ),
        Node(
            package='rviz2',#Launch file will call RViz itself
            executable='rviz2'
        )
    ])
