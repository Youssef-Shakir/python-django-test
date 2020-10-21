# class restaurant:
# 	def __init__(self,name,cusinse_type):
# 		self.name = name 
# 		self.cusinse_type = cusinse_typre
# 		self.number_served = 10
# 	def describe_resturant(self):
# 		print(f"this restaurant name is {self.name} and it is a {self.cusinse_type}")
# 	def restaurant_open(self):
# 		print(f"the {self.name} restaurant is now open")
# 	def number_served_c(self,num):
# 		self.number_served = num
# 	def incerment_served(self,num):
# 		self.number_served += num

# res_1 = restaurant('ahmed_falafel','wkateh')
# res_2 = restaurant('abo_majed','road')
# res_3 = restaurant('abo_amar','dirty')
# print(res_1.number_served)

class users:
	def __init__(self,first_name,last_name,age,location,email,password):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.email = email
		self.password = password
	def info(self):
		print(f"user name is : {self.first_name}\nlast_name is : {self.last_name}\nhis age is : {self.age}\nand his locatio is : {self.location}")
	def greet(self):
		print(f"hi {self.first_name}")
user_list = []
email_list = {}
while True:
	cmd = input("cmd : ")
	if cmd == 'help':
		print('quit to exist\nregister to create new user\nuser list to show users list')
	elif cmd == 'quit':
		break
	elif cmd == 'register':
		email_1 = input('email : ')
		password_1 = input('password : ')
		name_1 = input('name : ')
		last_1 = input('last : ')
		age_1 = input('age : ')
		location_1 = input('location : ')
		user_ne = users(name_1,last_1,age_1,location_1,email_1,password_1)
		user_list.append(user_ne)
		email_list[user_ne.email] = user_ne.password
	elif cmd == 'user list':
		for x in user_list:
			print(x)
	elif cmd == 'login':
		email_2 = input('email :')
		if email_2 in email_list.keys():
			password_2 = input('password : ')
			if password_2 == email_list[email_2]:
				print('you have sucsussfuly loged in')
				while True:
					cmd = input(f"cmd/{email_2}")
					articals = []
					if cmd == "add":
						artical = input('enter your artical')
					articals.append(artical)
					if cmd == 'articals':
						print(articals)
					if cmd == 'logout':
						break
					if cmd == 'my info':
						print(f"{user_ne.name()}")