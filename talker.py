#!/usr/bin/env python

# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rospy
from geometry_msgs.msg import Twist
import sys, select, os

if os.name == 'nt':
    import msvcrt, time
else:
    import tty, termios

BURGER_MAX_LIN_VEL = 0.12
BURGER_MAX_ANG_VEL = 2.84

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.5

e = """
Communications Failed
"""


# def getKey():
#     if os.name == 'nt':
#         timeout = 0.1
#         startTime = time.time()
#         while(1):
#             if msvcrt.kbhit():
#                 if sys.version_info[0] >= 3:
#                     return msvcrt.getch().decode()
#                 else:
#                     return msvcrt.getch()
#             elif time.time() - startTime > timeout:
#                 return ''

#     tty.setraw(sys.stdin.fileno())
#     rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
#     if rlist:
#         key = sys.stdin.read(1)
#     else:
#         key = ''

#     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
#     return key

def vels(target_linear_vel, target_angular_vel):
    return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel, target_angular_vel)


def makeSimpleProfile(output, input, slop):
    if input > output:
        output = min(input, output + slop)
    elif input < output:
        output = max(input, output - slop)
    else:
        output = input

    return output


# def constrain(input, low, high):
#     if input < low:
#       input = low
#     elif input > high:
#       input = high
#     else:
#       input = input

#     return input

# def checkLinearLimitVelocity(vel):
#     if turtlebot3_model == "burger":
#       vel = constrain(vel, -BURGER_MAX_LIN_VEL, BURGER_MAX_LIN_VEL)
#     else:
#       vel = constrain(vel, -BURGER_MAX_LIN_VEL, BURGER_MAX_LIN_VEL)

#     return vel

# def checkAngularLimitVelocity(vel):
#     if turtlebot3_model == "burger":
#       vel = constrain(vel, -BURGER_MAX_ANG_VEL, BURGER_MAX_ANG_VEL)
#     else:
#       vel = constrain(vel, -BURGER_MAX_ANG_VEL, BURGER_MAX_ANG_VEL)

#     return vel

if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    turtlebot3_model = rospy.get_param("model", "burger")

    target_linear_vel = 0.0
    target_angular_vel = 0.0
    control_linear_vel = 0.0
    control_angular_vel = 0.0

    try:
        while not rospy.is_shutdown():
            key = sys.argv[1]
            if key == 'w':
                # target_linear_vel = checkLinearLimitVelocity(target_linear_vel + LIN_VEL_STEP_SIZE)
                target_linear_vel = BURGER_MAX_LIN_VEL
            elif key == 'x':
                # target_linear_vel = checkLinearLimitVelocity(target_linear_vel - LIN_VEL_STEP_SIZE)
                target_linear_vel = -BURGER_MAX_LIN_VEL
            elif key == 'a':
                # target_angular_vel = checkAngularLimitVelocity(target_angular_vel + ANG_VEL_STEP_SIZE)
                target_angular_vel = BURGER_MAX_ANG_VEL
                # print(vels(target_linear_vel,target_angular_vel))
            elif key == 'd':
                # target_angular_vel = checkAngularLimitVelocity(target_angular_vel - ANG_VEL_STEP_SIZE)
                target_angular_vel = -BURGER_MAX_ANG_VEL
            elif key == 's':
                target_linear_vel = 0.0
                control_linear_vel = 0.0
                target_angular_vel = 0.0
                control_angular_vel = 0.0
            else:
                if (key == '\x03'):
                    break

            twist = Twist()

            control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (LIN_VEL_STEP_SIZE / 2.0))
            twist.linear.x = control_linear_vel;
            twist.linear.y = 0.0;
            twist.linear.z = 0.0

            control_angular_vel = makeSimpleProfile(control_angular_vel, target_angular_vel, (ANG_VEL_STEP_SIZE / 2.0))
            twist.angular.x = 0.0;
            twist.angular.y = 0.0;
            twist.angular.z = control_angular_vel

            pub.publish(twist)

    except:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0;
        twist.linear.y = 0.0;
        twist.linear.z = 0.0
        twist.angular.x = 0.0;
        twist.angular.y = 0.0;
        twist.angular.z = 0.0
        pub.publish(twist)

    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
