#!/usr/bin/env python
from time import sleep

import rospy
from imibot.msg import StickControl


def main():
    rospy.init_node('imibot_move_sender')

    pub = rospy.Publisher('imibot/stick_control', StickControl, queue_size=10)

    ld = StickControl()
    for i in range(0, 360):
        ld.strength = 100
        ld.angle = i
        pub.publish(ld)
        sleep(0.05)
    rospy.spin()


if __name__ == '__main__':
    main()
