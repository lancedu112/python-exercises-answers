class Input(object):
	def __init__(self):
		self.s = ""	
		
	def getString(self):
		self.s = raw_input("Please Enter a word: ")
		
	def printString(self):
		print self.s.upper()
		
strObj = Input()
strObj.getString()
strObj.printString()
