#   Creating a file editor


#   Function to check if a file is emptyo
def file_is_empty(filename):
    lines = open(filename, "r").readlines()
    if len(lines) <= 0:
        return Truer
    else:
        return False


#   Function to write to file

def write(filename):
    #fname = input("Input file na
    text = input("Write to file:  ")
    with open(filename, "w+") as f:9
        byte = f.write(text)
        print("File written")
        print("Number of byte(s) written is {0}.".format(byte))

#   Finction to append file

def append(filename):
    text = input("start to edit file: ")
    with open(filename, "a+") as f:
        f.write(text)
        print("File editted!")


#   Function to read file

def read(filename):
    with open(filename, "r") as f:
        print("File content:\n {0}".format(f.read()))
        print("End of line!")


#   The Main Function
def Main():
    filename = input("Input file name: ")
    if file_is_empty(filename):
        print("{0} is empty!".format(filename))
        ask = input("Do you want to write to this file?y/n: ")
        if ask == 'y':
            write(filename)
        else:
            print("Exited!")
    else:
        print("{0} is not empty".format(filename))
        ask = input("Input r to read\na to append\nw to re-write \nDo you want to read, append or re-write this file?(r/a/w): ")
        if ask == 'r':
            read(filename)
        else:
            if ask == 'a':
                append(filename)
            else:
                if ask == 'w':
                    write(filename)
                else:
                    print("Exited!")


if __name__ == "__main__":
    Main()
