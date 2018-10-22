#   Error Handling Exeptions

#   Exeptions are error that occur during the excution of a programme

#   Types Of Exceptions/Error

#   ValueError, IndexError, IndentError, OSError, NameError etc.

#   Example 1: How To Catch/Handle an Error with try/except keywords

#   A Dividing Calculatorsst

while True:
    nume = int(input("Input Numerator: "))
    denom = int(input("Input Deniminator: "))

    try:
        ans = int(nume/denom)
        log = "The answer of {0}/{1} is {2}".format(str(nume), str(denom), str(ans))
        print(str(log))
        with open("log.txt", "a+") as log:
            log.write("\n"+str(log))
            print("Log file written!\n")
    except ZeroDivisionError:
        print("An error occured")
        print("Division by zero")
        with open("log.txt", "a+") as log:
            log.write("Error occured\n")
            print("Log file written!\n")
