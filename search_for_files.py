import os

with open (r'item_codes_to_search.txt','r') as f:
	item_codes = f.read().splitlines()

path= 'D:\\'

with open('search_output.txt', 'w') as f:
		pass
with open('with_path.txt', 'w') as f:
	pass

for  item_code in item_codes:
	n = 0
	file_list=[]
	for root,dirs,files in os.walk(path):
		for file in files:
			if item_code in file:
				n += 1
				file_list.append(os.path.join(file))
				with open('pictures_full_path.txt', 'a') as f:
					f.write(os.path.join(root,file)+ "\n")
	print (item_codes.index(item_code)+1,"/",len(item_codes),": ",item_code," found ",n)
	with open('search_output.txt', 'a') as f:
		print (item_code,":",n,":",file_list, file = f)
