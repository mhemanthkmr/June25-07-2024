# def returnablefunction(a,b):
#     return a+b;
# print(returnablefunction(5,7))

########################################


def fullName (lastName, firstName) :
    return firstName + " " + lastName
print(fullName(firstName="Hemanth", lastName="Kumar"))


#####################################

# def nonReturnableFunction(a,b) :
#     return a + b;

# def returnableFunction(a,b) :
#     return a + b;
# print(returnableFunction(5,7))
# print(nonReturnableFunction(5,7))

################################################

# def argumentFunction(*arg) :
#     sum = 0
#     for i in arg :
#         sum += i
#     return sum

# print(argumentFunction(5,7,6,8,9,8,7,78,78,77,8,9))

###################################

# def returnableFunction(a,b=0) :
#     return a + b;
# print(returnableFunction(5,7))

#####################################

def argumentFunction(**arg) :
    print(arg['firstName'])
    print(arg['lastName'])
    print(arg['age'])

print(argumentFunction(firstName="Vijay", lastName="", age="45"))