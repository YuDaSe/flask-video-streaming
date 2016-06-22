
class TrackManeuver(object):

	MAX_DURATION = 3000
	MIN_DURATION = 1000

	MAX_DELTA = 4
	MIN_DELTA = -4

	"""
	Possible actions
	MANEUVER = 1
	CONTROL = 0
	"""

	ACTION_MANEUVER = 1

	def __init__(self, track, duration, delta):
		super(TrackManeuver, self).__init__()
		self.action = self.ACTION_MANEUVER
		self.setDuration(duration)
		self.setDelta(delta)
		self.track = track

	def setDelta(self, delta):
		if delta <= self.MAX_DELTA and delta >= self.MIN_DELTA:
			self.delta = delta

	def setDuration(self, duration):
		if duration <= self.MAX_DURATION and duration >= self.MIN_DURATION:
			self.duration = duration

	def getSerialMessage(self):
		return 'action:{action};duration:{duration};delta:{delta};track:{track}'.format(
			action=self.action,
			duration=self.duration,
			delta=self.delta + 5,
			track=self.track)