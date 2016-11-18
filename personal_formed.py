#!/usr/bin/env pytho
import sys
user = "jiahb"
sex = "male"
counter = 0
while True:
  if counter < 3:
	name = raw_input('please input your name:').strip()
        if len(name) == 0:
		print "empty name ,try again"
		continue
	#for i in range(0,3):
		#name = raw_input('please input your name:').strip()
	elif name == user:
		pass
	else:
		print "%s is not a valid user,try again" % name
         	       #counter = counter + 1
		counter += 1
		continue
	break
  else:
	sys.exit()
age = int(raw_input('please input your age:'))
gender = raw_input('please input your gender:').strip()
dep = raw_input('please input your dep:').strip()
message = '''the information of company staff
	name	: %s
	age  	: %s
	gender	: %s
	dep	: %s
	 ''' % (name , age , gender , dep)
print message
