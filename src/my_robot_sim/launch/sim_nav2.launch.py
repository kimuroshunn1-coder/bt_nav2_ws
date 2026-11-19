from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory
from launch.actions import TimerAction
import os


def generate_launch_description():

    pkg_dir = get_package_share_directory('my_robot_sim')

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_dir, 'launch', 'sim.launch.py')
        )
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_dir, 'launch', 'nav2.launch.py')
        ),
        launch_arguments={
            'follow': 'false'
        }.items()
    )

    return LaunchDescription([
      sim_launch,

      TimerAction(
         period=5.0,
         actions=[nav2_launch]
      )
    ])

