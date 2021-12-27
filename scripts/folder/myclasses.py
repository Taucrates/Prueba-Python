from mymain.main import mymethod

class BaseModel():
	def __init__(self, params = None):
		self.params = params
	def printme(self, message = "Hello, world"):
		print(message)

class printerobject(BaseModel):
	def __init__(self):
		self.printme()
# codigo
if __name__ == '__main__':
	print('your classes have been imported')
# mas codigo 
