class restaurant:
	def __init__(self,name,cusinse_type):
		self.name = name 
		self.cusinse_type = cusinse_type
		self.number_served = 10
	def describe_resturant(self):
		print(f"this restaurant name is {self.name} and it is a {self.cusinse_type}")
	def restaurant_open(self):
		print(f"the {self.name} restaurant is now open")
	def number_served_c(self,num):
		self.number_served = num
	def incerment_served(self,num):
		self.number_served += num















		++++++