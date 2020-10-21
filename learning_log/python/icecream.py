# class restaurant:
# 	def __init__(self,name,cusinse_type):
# 		self.name = name 
# 		self.cusinse_type = cusinse_type
# 		self.number_served = 10
# 	def describe_resturant(self):
# 		print(f"this restaurant name is {self.name} and it is a {self.cusinse_type}")
# 	def restaurant_open(self):
# 		print(f"the {self.name} restaurant is now open")
# 	def number_served_c(self,num):
# 		self.number_served = num
# 	def incerment_served(self,num):
# 		self.number_served += num

# class icecreamstand(restaurant):
# 	def __init__(self,name,cusinse_type):
# 		super().__init__(name,cusinse_type)
# 		self.flavors = ['strobery','apple','orange','tot']

# 	def show_flavors(self):
# 		print('we have the flowing flavors')
# 		for x in self.flavors:
# 			print(x)

# icecream = icecreamstand('icecreamstand','stand')

# icecream.show_flavors()

admin = ['can add users','can kick user','can ban user','can delete']
user = ['can join discusis','can make new post']

class users:
	def __init__(self,first_name,last_name,age,location,account_type):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.account_type = account_type
	def info(self):
		print(f"user name is : {self.first_name}\nlast_name is : {self.last_name}\nhis age is : {self.age}\nand his locatio is : {self.location}")
	def greet(self):
		print(f"hi {self.first_name}")

class pervilage:
	def __inti__(self):
		self.account_type = self.account_type
	def my_pervilage(self):
		self.account_type = account_type
		if self.account_type == "admin":
			print('your pervilage is ')
			for x in admin:
				print(x)
		if self.account_type == 'user':
			print('your pervilage is ')
			for x in user:
				print(x)

class admin(users):
	def __init__(self,first_name,last_name,age,location,account_type):
		super().__init__(first_name,last_name,age,location,account_type)
		self.prev = pervilage()

admin_user_1 = admin('youssef','shakir',17,'baghdad','admin')

admin_user_1.prev.my_pervilage('admin')






