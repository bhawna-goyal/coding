op ='''
press 1 for create single file:
press 2 for multiple file creation:
press 3 for touch -c command:
'''
print(op)
c=input("enter your choice : ")
if(c=='1'):
	file=input("enter file name:")
	f=open(file,'w')
	f.close()
	print("file created")
elif(c=='2'):
	n=int(input("enter the no. of files thay you want to create:"))
	l=[]
	for i in range(n):
		l.append(input("enter the name of file: "))
	for i in l:
		f=open(i,'w')
		f.close()
	print("file created successfully")
elif(c=='3'):
	a=input("enter file name:")
	print("command run successfully")
	exit()
else:
	print("invalid input")
