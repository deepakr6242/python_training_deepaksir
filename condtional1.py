
# marks = int(input('Enter the marks: '))

# if 70 < marks < 80:
#     print('check 70-75 category and 75-80 category ')
#     if 70 < marks < 75:
#         print('Average')
#     else:
#         print('above average')
# elif 75 < marks < 80:
#     print('above average')
# elif 80 < marks < 90:
#     print('Distinction')
# elif 90 < marks < 100:
#     print('elite')
# else:
    # print('poor students')


# to find the type of students based on marks--
# Reviewed below
marks = int(input('Enter the marks: '))

if 70 <= marks < 80:
	    print('checking 70-75 category and 75-80 category....... ')
	    if 70 <= marks <= 75:
	        print('Average')
	    else:
	        print('above average')
elif 80 <= marks <90:
	    print('Distinction')
elif 90 <= marks <=100:
	    print('elite')
elif 0 <= marks < 70:
	    print('Poor students')
else:
		print('Give valid marks within 100')
