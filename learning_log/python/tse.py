# while True:
# 	try:
# 		g = input('enter the cod : g / ')
# 		h = input('enter the cod : h / ')
# 		g = int(g)
# 		h = int(h)
# 		print(g+h)
# 	except ValueError9:
# 		print('provide string')


# dogs = open("dogs.txt",'r')
# dogs_name = dogs.read()
# print(dogs_name)


# try:
# 	cats = open('cats.txt',"r")
# 	cats_name = cats.read()
# 	print(cats_name)
# except FileNotFoundError:
# 	pass
import json

with open('data.json',"r") as ffk:
	data = json.load(ffk)

print(data)




