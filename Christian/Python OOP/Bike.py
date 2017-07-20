class Bike(object):
	"""docstring for ClassName"""
	def __init__(self, name, price, max_speed):
		self.name = name
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print self.name, "Price is: $" + str(self.price), "Top Speed: " + str(self.max_speed) + "mph", "Total miles: " + str(self.miles), "miles"
		return self

	def ride(self):
		self.miles += 10
		print "Riding" 
		print "Total miles", self.miles, "miles"
		return self

	def reverse(self):
		#avoid negative numbers
		if self.miles < 5:
			self.miles = 5
		self.miles -= 5
		print "Reversing"
		print self.miles, "miles"
		return self 



Honda = Bike("Honda", 5000, 180)
Honda.displayinfo().ride().ride().ride().reverse().displayinfo()

Yamaha = Bike("Yamaha", 8000, 200)
Yamaha.displayinfo().ride().ride().reverse().reverse().displayinfo

Suzuki = Bike("Suzuki", 4000, 150)
Suzuki.displayinfo().reverse().reverse().reverse().displayinfo()