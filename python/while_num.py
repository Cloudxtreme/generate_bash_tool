#!/usr/bin/env python
#*_* coding:utf-8 _*_
print_num=raw_input('which loop do you want to be:')

count = 0

while count < 10000:
	if print_num == count:
		print 'There you got the num:',count
		choice = raw_input('Do you want to continue? Y\N')
		if choice == 'n':
			break
		#else:
		#	while print_num <=count:
		#		print_num=raw_input('which loop do you want to continue:')
		#		print "it is over time"
else:
	print 'loop:',count
count +=1


