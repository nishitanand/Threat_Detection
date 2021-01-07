# importing os module 
import os 

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Function to rename multiple files 
def main(): 

	cwd=os.getcwd()
	print(cwd)
	#os.system("cd geeta_test")
	
	print(os.getcwd())
	for count,filename in enumerate(os.listdir("geeta")): 
		print("count",count, "filename", filename)
		if (count%2==0):
			random_val=get_random_string(8)
		if (count%2==0):
			dst=str(random_val) + ".jpg"
		else:
			dst=str(random_val) + ".txt"
		

		os.chdir(cwd+'\\geeta')
		src = str(filename) 
		dst = str(dst)  
		
		os.rename(src, dst)
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