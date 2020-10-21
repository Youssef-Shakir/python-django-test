# def greet_users(names):
# 	for x in names:
# 		print(f"hello {x}")
# na = ["youssef","ibrahem","ahmed"]
# greet_users(na)

# def printing(un_printed,complete):
# 	while un_printed:
# 		current_design = un_printed.pop()
# 		print(f"printing : {current_design}")
# 		complete.append(current_design)
# def printed(module):
# 	print(f"the flowing module has been printed")
# 	for x in module:
# 		print(x)

# unprinted_desings = ['phone case','robot pendant','dodecahedron']
# completed_modules = []

# printing(unprinted_desings[:],completed_modules)
# printed(completed_modules)

# print(unprinted_desings)





# def message_printer(un_message,printed):
# 	while un_message:
# 		current = un_message.pop()
# 		printed.append(current)
# def printer(mes):
# 	for x in mes:
# 		print(x)

# messages_unprinted = ['hi my name is youssef','hi i am from london','hi im im from fucking iraq and i hate my life :(']
# printed = []
# message_printer(messages_unprinted[:],printed)
# printer(printed)



# def make_pizza(size,*toppings):
# 	print(f'the pizza size is {size} and the flowing toppings will be add')
# 	for x in toppings:
# 		print(f"- {x}")


# make_pizza('18','chese','mushrooms','greens')
# def make_sandwitch(*topping):
#   	print('the flowing toppings will be added to your sandwitch')
#   	for x in topping:
#   		print(f"- {x}")

# make_sandwitch('tomato','ham','carote')
from im import make_profile
profile = make_profile('youssef','shakir',location='baghdad',tall=179)
print(profile)