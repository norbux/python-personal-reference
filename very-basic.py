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

###############
# Conditionals
###############
# if var == 'somfink':
#     print('whu-evah')
# elif var == 'somfn aeus':
#     print('yeah')
# else:
#     print('nuff')

##########################################
# Standard input
##########################################
# def addFromInput():
#     a = float(input("Enter first num:"))
#     b = float(input("Enter second num:"))
#     return a + b

# print(addFromInput())

#########################################
# Functions
#########################################
# def add(a, b):
#     return a + b

# print(add(3,2))

##########################################
# Loops
##########################################
# items = ["item 1", "item 2"]
# for item in items:
#     print(item)

# for number in range(1, 10):
#     print("Number {}".format(number))

# temp = 35
# while temp > 20:
#     print("too hot")
#     temp -= 1

# while temp > 20:
#     print("too hot")
#     temp -= 1
#     if temp == 10:
#         break

# for number in range(1, 10):
#     if number == 7:
#         print("We're skipping number 7")
#         continue
#     print("Number: {}".format(number))

# for number in range(1, 10):
#     if number == 3:
#         pass
#     print("Number: {}".format(number))


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

#######################################################
# Lists
#######################################################
# oneList = ["manzana", "pera", "naranja"]
# anotherList = [3, "123", 2.3, 654, "1993"]
# numbersList = [5, 3.4, 9, 6.589]
# print(oneList, anotherList)

# # oneList.append("platano")
# # print(oneList)

# oneList.extend(anotherList)
# print(oneList)

# anotherList.remove("1993")
# print(anotherList)

# anotherList.pop(4)
# print(anotherList)

# anotherList.pop(-1)
# print(anotherList)

# numbersList.sort()
# print(numbersList)

# boolVar = "ahuacate" in oneList
# print(boolVar)

# print(oneList.count("pera"))

# print(oneList.index("manzana"))

#######################################################
# Dictionaries
#######################################################
# settings = { "HP": 7, "Health": 8, "Speed": 6 }
# print(settings.get("Speed"))
# print(settings.items())
# print(settings.keys())
# print(settings.values())

# settings.popitem() # This removes the last item
# print(settings)

# settings.pop("HP") # This removes by index
# print(settings)

# settings.setdefault("Test", 1) # This adds an entry in the dict
# print(settings)

# moreSettings = { "Magic": 2, "Heal Factor": 4 }
# settings.update(moreSettings)
# print(settings)

# settings.update(Setting = 2, AnotherSetting = 1) # This adds or updates an existing item
# print(settings)

#######################################################
# Classes
#######################################################
# import random as random
# class Person:
#     def __init__(self, firstname, lastname, health, status):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.health = health
#         self.status = status

#     def introduce(self):
#         print("Hello, I'm {} {}".format(self.firstname, self.lastname))
    
#     def emote(self):
#         emotion = random.randrange(1, 3)
#         if emotion == 1:
#             print("{} is happy today".format(self.firstname))
#         elif emotion == 2:
#             print("{} is sad right now".format(self.firstname))
    
#     def status_change(self):
#         if self.health == 100:
#             print("{} is totally healthy".format(self.firstname))
#         else:
#             print("{} is not completelly healthy".format(self.firstname))

# Juan = Person("Juan", "Perez", 88, True)            
# print("{}'s status is {}".format(Juan.firstname, Juan.status))
# Juan.introduce()
# Juan.emote()
# Juan.status_change()

# class Cyborg(Person):
#     def __init__(self, model, firstname, lastname, health, status):
#         super().__init__(firstname, lastname, health, status)
#         self.model = model
    
#     def self_identify(self):
#         print("{}, Name: {}, Status: {}".format(self.model, self.firstname, self.status))


# t600 = Cyborg("T-600", "Arnold", "S", 100, True)
# t600.self_identify()
