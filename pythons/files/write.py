#   Witing To File
#   Firstly open the file in write i.e 'r'
#   To write into a file you have to use the write() method of the file object passing into as an argument the text to be written in the file

#   open the file in read mode.

myfile = open("hello.txt", "w")

print("File opened!")

#   Call the write method of the file

myfile.write("This file have been written")

print("File written!")

#   close the file

myfile.close()

print("File closed")

print("""\n""")

#   To make sure the file was written we have to read the file

myfile = open("hello.txt", "r")

print("File content:\n {0}".format(myfile.read()))

myfile.close()

