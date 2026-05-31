# the random access memory is volatile memory ,and all contents are loss once after program end 

# if we presist/save data   forever   we use file 

# a python can talk to the file by reading content from it and writing concept to it.

'''Types of file 
 Text file (txt,.c,etc)
 Binary file (.jpg,.dat,etc)
'''


f=open("D:/Python/Chapter9/file1.txt")  # Opens the file named "file.txt" in read mode (default)
data=f.read() #Reads the entire content of the file and stores it in the variable 'data'
print(data) # Prints the file content to the console
f.close()  # Closes the file to free system resources