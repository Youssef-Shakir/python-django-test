with open('text_file/text.txt') as file_object:
	lines = file_object.readlines()
string = ""
for x in lines:
	string += x.strip()

birthday = input('enter you birthday')
if birthday in string:
	print('yes your birthday is in the string')
else:
	print('no')

print(string)