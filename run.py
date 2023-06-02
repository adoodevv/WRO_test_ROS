#Program that uses wall follower and camera nodes to navigate

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

import rplidar
import RPi.GPIO as GPIO

import cv2
from cv_bridge import CvBridge, CvBridgeError

PORT_NAME = '/dev/ttyUSB0' # Replace with actual port name of the RPLidar
lidar = rplidar.RPLidar(PORT_NAME)

class WallFollower:
    def init(self):
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.process_scan)

        def process_scan(self, msg):
            #Process laser scan data to follow wall
            pass


class Camera:
    def init(self):
        self.sub = rospy.Subscriber('/camera/image_raw', Image, self.process_image)
        self.bridge = CvBridge()
        self.red_lower = (0, 0, 100)
        self.red_upper = (10, 10, 255)
        self.green_lower = (0, 100, 0)
        self.green_upper = (10, 255, 10)
        
        def process_image(self, msg):
            try:
                cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            except CvBridgeError as e:
                print(e)

            #Thresholding
            red_mask = cv2.inRange(bgr, self.red_lower, self.red_upper)
            green_mask = cv2. inRange(bgr, self.green_lower, self.green_upper)

            #Finding contours
            red_contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            #Drawing contours on image
            cv2.drawContours(cv_image, red_contours, -1, (0, 0, 255), 2)
            cv2.drawContours(cv_image, green_contours, -1, (0, 255, 0), 2)

            cv2.imshow('Image', cv_image)
            cv2.waitKey(3)


class Navigator:
    def init(self):
        self.wall_follower = WallFollower()
        self.camera = Camera()

        def run(self):
            rospy.init_node('navigator', anonymous = True)
            rate = rospy.Rate(10)

            while not rospy.is_shutdown():
                #Use data from wall follower and camera to make navigation decisions
                #Publish commands to control robot movement
                 cmd_vel = Twist()
                 cmd_vel.linear.x = 0.2
                 cmd_vel.angular.z = 0.1
                 self.wall_follower.cmd_vel_pub.publish(cmd_vel)
                 rate.sleep()

if name == 'main':
    navigator = Navigator()
    navigator.run()