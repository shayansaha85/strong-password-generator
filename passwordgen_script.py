import string as s
from random import *

length = int(input("Enter the length of your password : "))
password = ""

i = 0

ch = s.ascii_letters + s.digits + s.punctuation


while i<length:
	password += ch[randint(1,len(ch)-1)]
	i=i+1

try:
	file = open("password.txt", "w")
	file.write(password)
	file.close()
	print("Password generated")
except:
	print("Error")