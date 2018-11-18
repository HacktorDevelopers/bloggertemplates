#!  PYTHON PROGRAM

#   LISTS

print("A Program that upgrade student scores")

iscore = [22, 10, 16, 30, 10, 25, 35, 20, 4, 11]
tscore = 40
print("Initial Score")

def adtoscorse(lis, num):
    for i in lis:
        res = list(map(lambda x: x+num, lis))
        print(res)

num = 1

for i in iscore:
    perc = int((i/tscore)*100)
    if perc < 50:
        print(str(num)+" --- Failed with "+ str(perc)+"%")
    else:
        print(str(num)+" --- Passed with "+ str(perc)+"%")
    num += 1
    
    #if ((i/tscore)+100) < 70:
    #print("Thstis Faied"
