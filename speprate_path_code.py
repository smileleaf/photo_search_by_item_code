import os

with open (r'pictures_full_path.txt','r') as f:
	lines_list = f.readlines()

with open ('pictures_sperate_path.csv', 'w') as f:
	for line in lines_list:
		path,filename = os.path.split(line)
		filename, ext = os.path.splitext(filename)
		f.write(f'{path}, {filename}, {ext}')