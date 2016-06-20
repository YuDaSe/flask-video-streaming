
class TrackControl(object):

	MAX_LEFT= 5
	MIN_LEFT= -5

	MAX_RIGHT= 5
	MIN_RIGHT= -5

	def __init__(self, left, right):
		super(TrackControl, self).__init__()
		self.left = left
		self.right = right

	def setLeft(self, left):
		if left <= self.MAX_LEFT and left >= self.MIN_LEFT:
			self.left = left

	def getLeft(self):
		return self.left

	def setRight(self, right):
		if right <= self.MAX_RIGHT and right >= self.MIN_RIGHT:
			self.right = right

	def getRight(self):
		return self.right

	def getSerialMessage(self):
		return 'left:{left};right:{right}'.format(left=self.left + 5, right=self.right + 5)