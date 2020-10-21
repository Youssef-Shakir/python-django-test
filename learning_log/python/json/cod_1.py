import json
fav_num = input('enter your faviourit number / ')
fav_num = int(fav_num)

with open('fav_num.json','w') as f:
	json.dump(fav_num,f)