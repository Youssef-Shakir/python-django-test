from random import randint
from random import choice
# print(randint(1,9))
# pi = ['h','youssef','ibrahem']

# print(choice(pi))

# class die:
# 	def __init__(self,die=6):
# 		self.die = die
# 	def roll_die(self):
# 		print(randint(0,6))

# rol = die()

# rol.roll_die()
# lotry = [1,2,3,4,5,6,7,8,9,'a','s','x','g']
# def roller():
# 	lotry = ['1','2','3','4','5','6','7','8','9','a','s','x','g']
# 	rol = f"{choice(lotry)}{choice(lotry)}{choice(lotry)}{choice(lotry)}"
# 	return rol
# my_ticket = f"1x2g"
# print(f"my ticket is {my_ticket}")
# triyes = 0
# while True:
# 	lotr = roller()
# 	if lotr == my_ticket:
# 		print(f'you win with {triyes}')
# 		print(lotr)
# 		break
# 	else:
# 		triyes += 1
# 		print(f"lotry was {lotr}\ntry number : {triyes}")

def gen():
	rol = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z',1,2,3,4,5,6,7,8,9]
	get = f"{choice(rol)}{choice(rol)}{choice(rol)}{choice(rol)}"
	return get
genr = gen()
cod_list = []
new_cods = []
dub = 0
file_name = input('enter exicting file name / ')
with open(file_name,'r') as cods_file:
	content = cods_file.readlines()
for x in content:
	cod_list.append(x.rstrip())
cods_file.close()

while True:
	cmd = input('cmd / ')
	if cmd == 'help':
		print('type start to start the genrator\ntype print to see the result')
	if cmd == 'start':
		ins = input('enter the amount of cods you want to genrate : ')
		ins = int(ins)
		trys = 0
		dub = 0
		i = 0
		while trys <= ins:
			genr = gen()
			genr = f"{genr}\n"
			if genr not in cod_list:
				new_cods.append(genr)
				trys += 1
			else:
				dub += 1
				i += 1
			if dub == 500 or dub == len(new_cods)-2000:
				dub = len(new_cods)
			if i == 100:
				i=0
				print(f"dub {dub} len {len(new_cods)}")

			if dub == len(new_cods)+500:
				break
			cods_file.close()
	if cmd == 'print':
		print(cod_list)
	if cmd == 'quit':
		break
	if cmd == 'len':
		print(len(cod_list))
	if cmd == 'new len':
		print(len(new_cods))
	if cmd == 'new cods':
		print(new_cods)
	if cmd == 'write':
		new_append = open(file_name,'a')
		for x in new_cods:
			new_append.write(x)
# file_name = input('enter the file name / ')
