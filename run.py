#Program that uses wall follower and camera nodes to navigate

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

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
        
        def process_image(self, msg):
            #Process image data to detect obstacles
            pass


class Navigator:
    