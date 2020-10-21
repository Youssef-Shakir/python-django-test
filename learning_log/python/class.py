# class dog:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age

# my_dog = dog('gogo',8)

# print(f"my dog name is {my_dog.name}")

# class restaurant:
# 	def __init__(self,name,cusinse_type):
# 		self.name = name 
# 		self.cusinse_type = cusinse_type
# 	def describe_resturant(self):
# 		print(f"this restaurant name is {self.name} and it is a {self.cusinse_type}")
# 	def restaurant_open(self):
# 		print(f"the {self.name} restaurant is now open")

# res_1 = restaurant('ahmed_falafel','wkateh')
# res_2 = restaurant('abo_majed','road')
# res_3 = restaurant('abo_amar','dirty')

# res_1.describe_resturant()
# res_2.describe_resturant()
# res_3.describe_resturant()

class users:
	def __init__(self,first_name,last_name,age,location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
	def info(self):
		print(f"user name is : {self.first_name}\nlast_name is : {self.last_name}\nhis age is : {self.age}\nand his locatio is : {self.location}")
	def greet(self):
		print(f"hi {self.first_name}")
user_list = []
while True:
	cmd = input("cmd : ")
	if cmd == 'help':
		print('quit to exist\nnew user to create new user\nuser list to show users list')
	elif cmd == 'quit':
		break
	elif cmd == 'new user':
		name_1 = input('name : ')
		last_1 = input('last : ')
		age_1 = input('age : ')
		location_1 = input('location : ')
		user_ne = users(name_1,last_1,age_1,location_1)
		user_list.append(user_ne)
	elif cmd == 'user list':
		for x in user_list:
			print(x)
