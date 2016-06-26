import unittest

import sys
import os
sys.path.append(os.path.join('..', 'src'))

from classes.TrackControl import TrackControl

class TestTrackControl(unittest.TestCase):

    def test_track(self):
        tc = TrackControl(0, 0)
        self.assertEqual(tc.getLeft(), 0)

    def test_serial_message(self):
    	tc = TrackControl(0, 0)
    	self.assertEqual(tc.getSerialMessage(), 'action:0;left:5;right:5')

    def test_to_json(self):
    	tc = TrackControl(0, 0)

    	self.assertEqual(tc.to_json(), '{"action": 0, "left": 0, "right": 0}')

