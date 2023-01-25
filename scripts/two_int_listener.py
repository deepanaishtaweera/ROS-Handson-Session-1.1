#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16

# START CODE HERE #
# TODO: Import the created msg file

# END CODE HERE #


def callback(data):
    # START CODE HERE #
    # TODO: Complete callback function
    global pub

    total = None
    rospy.loginfo(None + " + " + None +
                  " = " + str(total.data)+"\n")
    pub.publish(total)
    # END CODE HERE #


def talker_listener():

    # START CODE HERE #
    # TODO: Create a ros node named 'two_ints_listner_node'
    
    # END CODE HERE #

    global pub

    # START CODE HERE #
    # TODO: 
    # 1. Define the publisher 'pub' to publish '/sum' topic
    # 2. Call the rospy.Subscriber() with topic, dtype and callback
    pub = None


    # END CODE HERE #

    rospy.spin()


if __name__ == '__main__':
    try:
        talker_listener()
    except rospy.ROSInterruptException as e:
        raise e
