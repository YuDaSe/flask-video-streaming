
class Serial(object):

	def __init__(self, dev, port):
		super(Serial, self).__init__()
		print dev
		print port

	def write(self, data):
		print data
