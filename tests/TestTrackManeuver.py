import unittest

import sys
import os
sys.path.append(os.path.join('..', 'src'))

from classes.TrackManeuver import TrackManeuver

class TestTrackManeuver(unittest.TestCase):

    def test_track(self):
        tm = TrackManeuver("left", 1000, 2)

        self.assertEqual(tm.duration, 1000)
        self.assertEqual(tm.track, "left")
        self.assertEqual(tm.delta, 2)

    def test_serial_message(self):
    	tm = TrackManeuver("left", 1000, 2)
    	self.assertEqual(tm.getSerialMessage(),
    		'action:1;duration:1000;delta:7;track:left')
