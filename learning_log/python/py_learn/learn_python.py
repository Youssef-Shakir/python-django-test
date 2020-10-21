# file_name = 'learn.txt'
# with open(file_name) as text:
# 	content = text.readlines()
# text_str = ''
# for x in content:
# 	text_str += x.replace('python','c')
# print(text_str)

file_name = "guest.txt"

with open(file_name,"w")as guests:
	while True:
		name = input("enter your name : ")
		user = guests.write(f"{name}\n")
		if name == "quit":
			break