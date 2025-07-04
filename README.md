# hdl-localization-ROS2 (humble, without Docker)

[ROS2 humble] HDL 3D LiDAR localization package 

The following package is a version of hdl-localization-ROS2 built for the Humble distribution without using Docker.
You can refer to the original [hdl localization repository](https://github.com/koide3/hdl_localization.git) for a detailed explanation of the ROS1 version.


## TO DO
To use your own data, modify the path to the PCD file, IMU topic, and LiDAR topic in the file 'hdl-localization-ROS2/hdl_localization/launch/hdl_localization_2.launch.py'.

You can make the changes as shown below:

'''
    points_topic = LaunchConfiguration('points_topic', default='/velodyne_points')
    odom_child_frame_id = LaunchConfiguration('odom_child_frame_id', default='velodyne')
    imu_topic = LaunchConfiguration('imu_topic', default='/imu/data')
    globalmap_pcd = DeclareLaunchArgument('globalmap_pcd', default_value='/home/path/of/map.pcd', description='Path to the global map PCD file')
'''

Also, be sure to update the 'remappings' section accordingly:

''' 
('/velodyne_points', points_topic),('/imu/data', imu_topic) 
'''

## Acknowledgement
- [DataspeedInc/hdl_localization](https://github.com/DataspeedInc/hdl_localization/tree/ros2)   
- [DataspeedInc/hdl_global_localization](https://github.com/DataspeedInc/hdl_global_localization/tree/ros2)  
- [DataspeedInc/fast_gicp](https://github.com/DataspeedInc/fast_gicp/tree/ros2)
- [tier4/ndt_omp](https://github.com/tier4/ndt_omp)  
