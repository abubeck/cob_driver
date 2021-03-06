#!/usr/bin/env python
import roslib; roslib.load_manifest('cob_relayboard')
import rospy
import time
from cob_relayboard.msg import EmergencyStopState
from std_msgs.msg import Float64

def relayboard_sim():
	rospy.init_node('cob_relayboard_sim')

	# emergency_stop topic
	pub_em_stop = rospy.Publisher('/emergency_stop_state', EmergencyStopState, queue_size=1)
	msg_em = EmergencyStopState()
	msg_em.emergency_button_stop = False
	msg_em.scanner_stop = False
	msg_em.emergency_state = 0

	# power_board/voltage topic
	pub_voltage = rospy.Publisher('/power_board/voltage', Float64, queue_size=1)
	msg_voltage = Float64()
	msg_voltage.data = 48.0 # in simulation battery is always full

	while not rospy.is_shutdown():
		pub_em_stop.publish(msg_em)
		pub_voltage.publish(msg_voltage)
		rospy.sleep(1.0)

if __name__ == '__main__':
	try:
		relayboard_sim()
	except rospy.ROSInterruptException:
		print "Interupted"
		pass
