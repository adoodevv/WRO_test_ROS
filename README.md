# WRO_test_ROS
Official test repository for TEAM MAGNUS using ROS

## run program explanation
1. Program creates three classes : WallFollower, Camera, and Navigator

2. The WallFollower class subscribes to the /scan topic to recieve laser scan data and uses data to follow the inner wall

3. The Camera class subscribes to the /camera/image_raw topic to recieve image data and uses the data to data to detect red and green objects

4. The Navigator class creates instances of the WallFollower and Camera classes, and uses their data to make naviagtion decisions. It then publishes the commands to the /cmd_vel topic to control the robot's movement

5. The run method of the Navigator class is called in the main block of the program. This method initializes the ROS node, sets the rate of the loop, and repeatedly uses data from the wall follower and camera to make navigation decisions and publish commands to control the robot's movement