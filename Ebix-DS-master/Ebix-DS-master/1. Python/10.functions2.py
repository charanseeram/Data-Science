#Functions

#There is no begining and end in the python. Just indentation decides the begining and end.
#In python, coding is simnplified
def add(a,b,c):
    tmp = a+b
    tmp = tmp + c
    return tmp

print(add(10,20,30))

#Functions with optional arguments
def addWithOptionalArgs(a,b=10,c=20):
    tmp = a+b
    tmp = tmp + c
    return tmp

print(addWithOptionalArgs(5,c=26)) #Here the output will be 5+b=10+26 = 41
#Note that parameter name is compulsion(C in above example) when you want to skip some parameter(skipped b in above example). 
#Otherwises parameter name is not required
