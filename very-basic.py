# Single line comment...

"""
Multi-line comment..
...
"""

#####################################
# String formating and interpolation
#####################################
# text1 = "Hell"
# text2 = "world"
# formated = "{}, oh {}".format(text1, text2)
# print(formated)

############
# Functions
############
# def add(a, b):
#     return a + b

# print(add(3,2))

#################
# Standard input
#################
# def addFromInput():
#     a = float(input("Enter first num:"))
#     b = float(input("Enter second num:"))
#     return a + b

# print(addFromInput())

#######################################################
# Arguments: Args, Kwargs (key word arguments), *args
#######################################################
# def normalArgs(name, age):
#     # This function takes required arguments
#     print("{} is {} old".format(name, age))

# normalArgs("Juan", 21)

# def normalArgs(name = "Juan", age = 5):
#     # This function takes keyword/default arguments
#     print("{} is {} old".format(name, age))

# normalArgs("Pedro")

# def normalArgs(name, age, *args, **kwargs):
#     # This function takes any number of args after the required ones
#     # (*args) and also takes any number of keyword arguments after the *args
#     kwa = ""
#     for arg in kwargs.values():
#         kwa += arg

#     print("{} is {} years old, lives in {} and stinks like {}".format(name, age, args[0], kwa))

# normalArgs("Steve", 21, "Mars", smell = "onions")