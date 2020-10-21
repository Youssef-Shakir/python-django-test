import json
try:
	with open('fav_num.json') as f:
		fav_num = json.load(f)

except FileNotFoundError:
	fav_num = input('enter your faviourit number / ')
	fav_num = int(fav_num)

	with open('fav_num.json','w') as f:
		json.dump(fav_num,f)
else:
	print(f'your favoiurit number is / {fav_num}')