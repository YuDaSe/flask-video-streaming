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
    	self.assertEqual(tc.getSerialMessage(), 'left:5;right:5')
