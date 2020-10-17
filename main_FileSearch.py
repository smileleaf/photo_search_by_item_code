'''
The code will look for files that contain in their name the item code
output:

*search_summary.txt*
Is a summary that mention how many pictures found for each item 

*pictures_full_path.txt*
each line has the item code, and complete path (splitted) of the image file
to be used in excel (it is comma separated)
'''

#config

#from where to start search
path= 'D:\\'

#imports
import os


# reads the file with the item code
with open (r'item_codes_to_search.txt','r') as f:
	#saved to a list of codes
	item_codes = f.read().splitlines()


#this method creates a new empty file for the output
#because next in the code I will be appending to it
#so it is important to start with a clean file
with open('search_summary.txt', 'w') as f:
		pass
#same as above. clean file.
with open('pictures_full_path.txt', 'w') as f:
	pass

for  item_code in item_codes:
	#reset counter and list with each item code
	n = 0
	file_list=[]
	for root,dirs,files in os.walk(path):
		for file in files:
			if item_code in file:
				n += 1
				#creating the file list for the current item code
				file_list.append(os.path.join(file))
				#writing the full path for the current one file found
				with open('pictures_full_path.txt', 'a') as f:
					filename, ext = os.path.splitext(file)
					f.write(item_code + ',' + root + ',' + filename + ',' + ext + "\n")
	
	#updated after each item code search
	

	#Update the user
	print (item_codes.index(item_code)+1,"/",len(item_codes),": ",item_code," found ",n)
	
	#if nothing found then n=0 and file_list=[]
	with open('search_summary.txt', 'a') as f:
		#file = f direct the output to the file
		print (item_code,":",n,":",file_list, file = f)