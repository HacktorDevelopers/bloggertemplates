#   Reading file content
#To Read File Content, the file have to be opened in read mode

myfile = open("hello.txt","r")

print("File openned!")

#   Assign the file content to a variable

fcont = myfile.read()

print("File content gotten!")

#   Print the file content

print(fcont)

print("File have been read!")

#   File lines can also be read by calling the readlines method

lines = myfile.readlines()

if len(lines) <= 0:
    print("File is empty!")
else:
    print("The number of lines = {0}".format(len(lines)))

#   close the file

myfile.close()

print("File closed!")
