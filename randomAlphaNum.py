import string
from random import *
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) 	
print("This is your password : ",password)