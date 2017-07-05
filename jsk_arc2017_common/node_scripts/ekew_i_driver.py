#!/usr/bin/env python

import serial

import rospy
from std_msgs.msg import Float32


class EkEwIDriver(object):

    """Read data from EK-i/EW-i scale.

    Data Sheet: https://www.aandd.co.jp/adhome/pdf/manual/balance/ekew-i.pdf
    """

    def __init__(self):
        super(EkEwIDriver, self).__init__()
        port = rospy.get_param('~port', '/dev/ttyUSB0')
        rospy.loginfo('port=%s', port)
        # EK-i/EW-i series default settings
        self.ser = serial.Serial(
            port, baudrate=2400, bytesize=7, parity=serial.PARITY_EVEN)
        self.pub = rospy.Publisher('~output', Float32, queue_size=1)
        rate = rospy.get_param('~rate', 10)
        self.read_timer = rospy.Timer(rospy.Duration(1. / rate),
                                      self._read_timer_cb)

    def _read_timer_cb(self, event):
        if self.pub.get_num_connections() == 0:
            return

        self.ser.write('Q\r\n')
        data = self.ser.read(17)

        header = data[:2]
        if header == 'ST':
            # scale mode
            weight = float(data[3:12])
            unit = data[12:15]
            if unit != '  g':
                rospy.logerr('Unsupported unit: %s', unit)
                return
            msg = Float32(data=weight)
            self.pub.publish(msg)
        elif header == 'QT':
            # number mode
            rospy.logerr('Unsupported mode: %s', header)
            return
        elif header == 'US':
            # unstable
            return
        elif header == 'OL':
            # scale over
            rospy.logerr('Scale over')
            return


if __name__ == '__main__':
    rospy.init_node('ekew_i_driver')
    EkEwIDriver()
    rospy.spin()
