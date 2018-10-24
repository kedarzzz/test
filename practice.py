import sys
import re

word = "[A-Z][a-z]"
name=0
passwd=0
name = str(raw_input("Please enter username: "))
while not re.findall("^[A-Za-z]*$", name):
#if re.match("^[A-Za-z]*$", name):
	print "Please enter letters"
	name = raw_input("Please enter username: ")

while True:
	if len(name) < 6:
		print "Please use atleast 6 alphabets"
		name = raw_input("Please enter username: ")
	else:
		break

passwd = raw_input("Please enter password: ")
#while True:
#	passwd = raw_input("Please enter password: ")
#	if len(passwd) < 6:
	#	print "Print Please enter password with minimum of 6 character."
	#	break
print "Hello " +name	
if passwd == "hello1":
	print "Access Granted."
	print "Welcome to the System."
else:
	attempt = 0
	while True:
		tryAgain = raw_input("Please enter correct password: ")
		if tryAgain	== "hello1":
			print "You are in"
			break	
		else:	
			attempt = attempt + 1
			if attempt == 3:
				print "You tried password more than 3 times, now the system will now terminate."		
				break
	while True:
		response=raw_input("Type exit to exit: ")
		if response == 'exit':
			sys.exit()




#	raise SystemExit

#		else:
#			if tryAgain == "hello":
#				print "You are in "
#				break






