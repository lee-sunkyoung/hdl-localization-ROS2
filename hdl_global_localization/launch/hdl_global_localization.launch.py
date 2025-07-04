# <?xml version="1.0"?>
# <launch>
#   <!-- load params -->
#   <rosparam command="load" file="$(find hdl_global_localization)/config/general_config.yaml" ns="/hdl_global_localization" />
#   <rosparam command="load" file="$(find hdl_global_localization)/config/bbs_config.yaml" ns="/hdl_global_localization" />
#   <rosparam command="load" file="$(find hdl_global_localization)/config/fpfh_config.yaml" ns="/hdl_global_localization" />
#   <rosparam command="load" file="$(find hdl_global_localization)/config/ransac_config.yaml" ns="/hdl_global_localization" />
#   <rosparam command="load" file="$(find hdl_global_localization)/config/teaser_config.yaml" ns="/hdl_global_localization" />


#   <node pkg="hdl_global_localization" type="hdl_global_localization_node" name="hdl_global_localization" output="screen" />
# </launch>

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescriptionwef
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('hdl_global_localization')

    param_files = [
        os.path.join(pkg_share, 'config', 'general_config.yaml'),
        os.path.join(pkg_share, 'config', 'bbs_config.yaml'),
        os.path.join(pkg_share, 'config', 'fpfh_config.yaml'),
        os.path.join(pkg_share, 'config', 'ransac_config.yaml'),
        os.path.join(pkg_share, 'config', 'teaser_config.yaml'),
    ]

    return LaunchDescription([
        Node(
            package='hdl_global_localization',
            executable='hdl_global_localization_node',
            name='hdl_global_localization',
            output='screen',
            parameters=param_files,
        )
    ])
