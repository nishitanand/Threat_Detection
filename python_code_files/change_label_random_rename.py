# importing os module 
import os 

import random
import string

# Function to rename multiple files 
def main(): 

	cwd=os.getcwd()
	print(cwd)
	#os.system("cd geeta_test")
	
	print(os.getcwd())
	for count,filename in enumerate(os.listdir("geeta_test")): 
		print("count",count, "filename", filename)
		
		os.chdir(cwd+'\\geeta_test')

		if (count%2!=0):
			with open(filename,"r") as myfile:
				data=myfile.readlines()

			#print(type(data))
			#print(data)
			data=data[0].split(" ")
			#print(data)
			# 3 for geeta and 2 for niyati
			data[0]="3"
			#print(data)
			
			def listTostring(s):  
				string = " "
				# return string 
				return (string.join(data))  
			
			str_new=listTostring(data) 


			f1=open(filename,"w")
			f1.write(str_new)
			f1.close()

		
		
		
		# rename() function will 
		# rename all the files 
		
		
		print(os.getcwd())
		os.chdir(cwd)
		print(os.getcwd())


# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 




#get_random_string(8)
#get_random_string(8)
#get_random_string(6)