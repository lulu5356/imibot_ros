#!/usr/bin/env python
import rospy
from location_monitor.msg import StickControl
from control_handler import ControlHandler


def main():
    controls_handler = ControlHandler()
    rospy.init_node('imibot_move')
    rospy.Subscriber("location_monitor/stick_control", StickControl, controls_handler.move)
    rospy.spin()


if __name__ == '__main__':
    main()
