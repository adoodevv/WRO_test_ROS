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