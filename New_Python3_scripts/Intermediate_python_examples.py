# ################################################################################
# string operation
# x = 12
# phrase = "hi joseph"
# print (phrase.split(' '))
# print (phrase.strip('hi '))
# print (phrase.replace('hi', 'buy'))
# print (phrase.splitlines('hi'))

# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print (phrase.find('hi'))
# print(phrase.find('hi'))


# built in Functions
# print (type(x))
# print (len(phrase))
# ##################################################################

# LISTS and thier operations

# from functools import lru_cache
# fruits = ["oragne", "banana", "apples", "melons"]

# fruits.append("kiwi")
# print (fruits)

# fruits.sort()
# print (fruits)

# fruits.insert(4, "tangerine")
# print (fruits)

# fruits.pop()
# print (fruits)

# fruits.remove("oragne")
# print (fruits)

# vegi = ["carrots", "tomatoes"]
# fruits.extend(vegi)
# print (fruits)

# new_list = fruits.copy()
# print(new_list)

# fruits.reverse()
# print (fruits)

# reverse = fruits[::-1]
# print(fruits)


# these 2 methods doe not follow the convension

# x = fruits.count("banana")
# print(x)

# x = fruits.index("banana")
# print (x)

# #################################################################

# Tuples and their operations

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# use index notation to return element of a tuple, jsut like list
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# looping thurouhg a tuple
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# check to see if an element exist in a tuple

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#     print ("yes 'apple' is in tuple")

# finding out the length of a tupple
# print (len(thistuple))

# TIS IS GATCHU ( To create a tuple with only one item,
# you have to add a comma after the item, otherwise
# Python will not recognize it as a tuple.)

# single_tuple = ("apples",)
# print (single_tuple)

# to add 2 tuples you simply add them together

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# to find the length of a tuple use the len function

# x = len(tuple1)
# print (x)

# to remove tuple use the del function in python

# del (tuple1)
# print (tuple1)
# there are 2 mehtods for tuples.

# cound and index

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(7)

# print(x)

# # Index

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(8)

# print(x)

# exercise: find the average of these numbers in this list

# test_yourself = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]

# size = len(test_yourself)
# print (size)

# total = sum(test_yourself)
# print (total)


# avarage = (sum(test_yourself)/len(test_yourself))
# print (avarage)

# Functions

# def my_function(*kids):
#   print("I have " + kids+ " children")

# my_function("Joe", "Tobias")


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))


# try:
#   print(x)
# except First_error:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# for i in range(5):
#     print(i)

# you can pass number of argument to a function using the (*) in your argument
# def multiply (*number):
#     total = 1
#     for elem in number:
#         total = total * elem
#     return total


# print (multiply(2, 5, 8, 7))


# you can pass a dictionary to your funtion by using the ** in your argument
# def save_user(**user):
#     print (user["name"])


# save_user(ide=1, name="admin")

# def fizbuz(input):
#     if (input % 3== 0) or (input % 5 == 0):
#         return fizbuz
#     elif input % 3 == 0:
#         return fiz
#     elif input % 5 ==0:
#         return buz
#     else:
#         return input


# print (input(7))

# Classes
# a function inside a class is called a method


#  import datetime

#  class User:
#     """this is where your documentation goes"""

#     def __init__(self, full_name, birthday):
#         self.full_name = full_name
#         self.birthday = birthday
#         #x = 5
#         #super().__init__()

#         #extract first and last name
#         name_peices = full_name.split(" ")
#         self.first_name = name_peices[0]
#         self.last_name = name_peices[-1]

# user1 = User("Joseph Mousa", "06-17-1980")         #this is how you create a instance of an object

# print (user1.full_name, user1.birthday)
# print (user1.first_name, user1.last_name)




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     self.x = 5

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# print(p1.name)
# print(p1.age) 
# print(p1.x)




# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# x = Person("John", "Doe")
# x.printname() 

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()

# Use the Person class to create an object, and then execute the printname method:


# print(myfunc)







# fininotic serioes


# @lru_cache(maxsize=100)
# def febonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return febonacci(n-1) + febonacci(n-2)


# for n in range(1-501):
#     print(n, ":", febonacci(n))

# list comprehensions

# squares = []
# for i in range(1-101):
#     squares.append(i**2)


# print (squares)

# squares = [i**2 for i in range(10)]
# print(squares)

# number_list = [x ** 2 for x in range(10) if x % 2 == 0]
# print(number_list)

# with open("data.txt") as fh:
#     my_bio = fh.read()

# print (my_bio)


# with open("data.txt") as f:
#   myFile = f.read()

# print (myFile)     #this will print out the entire file


# for ele in myFile:  # this will print the file one char at a time
#   print (ele)

# with open("data.txt") as f:
#    myFile = f.readline()

# print (myFile)

# for ele in myFile:
#     print (ele)     # this will print each line of the file


# with open("data.txt") as f:
#     myFile = f.readlines()


# for ele in myFile:
#   print (ele)






#print (myFile)

  







def



