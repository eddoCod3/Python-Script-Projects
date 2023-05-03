

""" 
number_valid = 4
number_center = 5
name  = input("Give me you name : ")
def something(x,y):
    return x+y


def myfunction(x,y):
    return ((x*y) + y)


for i in range(number_center):
        print(i)


print ("--------------------------------")
print(something(number_valid, number_center))
print(myfunction(number_valid, number_center))
print("Your name is : "+ name)
"""

def simple__calc():
    operation = input("what operation want to perform : ")
    x = int(input("First number: "))
    y = int(input("Second numbe:  "))
    
    if operation == "+":
        return x +y
    elif operation == "-":
        return x -y
    elif operation =="*":
        return x * y
    else:
        return x/y


print(simple__calc())