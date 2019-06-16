#for cat command 
file=open("cat1.txt","r")
print(file.read)

#for cat -e command
for line in file:
	print(line.strip()+"$")

#for cat -n command
count = 1
for line in file:
	print(str(count)+line.strip())
	count+=1

#for output redirection -overwrite
loc=input("enter the file to be overwritten : ")
file1  = open(loc,"w")
file1.write(file.read())
print(file1)
file1.close

#for output redirection - append
file.seek(0)
loc1 = input("enter the fiel to be append :")
file2 = open(loc1,"a")
file2.write(file.read())
file.close()
file2.close()
