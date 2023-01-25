#!/usr/bin/env python
import random

import rospy

# START CODE HERE #
# TODO: Import the created msg file

# END CODE HERE #


def talker():
    # START CODE HERE #
    # TODO: Create a publisher for the topic '/two_ints'
    pub = None
    # END CODE HERE #
    rospy.init_node('two_int_talker_node', anonymous=True)

    # START CODE HERE #
    # TODO: Define r to publish a message once in every 2 seconds
    r = None
    # END CODE HERE #

    rate = rospy.Rate(r)
    random.seed()

    while not rospy.is_shutdown():

        # START CODE HERE #
        # TODO: Create a msg with the correct dtype
        msg = None
        # END CODE HERE #

        msg.a = None  # TODO: Generate a random number between 1 and 20
        msg.b = None  # TODO: Generate a random number between 1 and 20
        rospy.loginfo(f"{msg.a} and {msg.b} are published")
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
