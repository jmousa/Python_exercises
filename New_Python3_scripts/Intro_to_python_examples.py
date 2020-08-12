# print("Hello world")
# student_count = 100
# print('*' * 10)
# print(student_count)
# rating = 4.00  # float
# is_published = False
# message = """ hi mosh this is joseh
# """
# course = 'programming'
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:])
# print(course[:3])
# print(course[::-1])  #this will reverse the string
# print(course[1:-1])  # this will give you the entire string except the first and last letter

# course = "python programming"

# first = 'joe'
# last = 'mousa'
#full = (first + " " + last)
# full = (f"{len(first)} {last}")
# print (f"hi {first} and hi {last}")
# print (full)
# print (course.upper())
# print (course.lower())
# print (course.title())
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
# print(course.find("pro"))  # return the index
# print(course.replace("p", "j"))
# print("pro" in course)   # this return True
# print("swift" not in course)

# numbers

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)   # 3.3333
# print(10 // 3)  # 3
# print(10 % 3)   # gives you the remainder
# print(10 ** 3)  # exponent = 1000

# print (round(2.5))
# print (abs(-2.9))

# import math

# search google for
# python 3 math module


# the follwoing are used for convresion
# int(x)
# float(x)
# bool(x)
# str(x)
# type(x) will return the type of x

# the following is false in boolean context
# ""
# 0
# None
# naything else is True

# x = bool(None)
# print (x)

# comparison operators
# <
# <=
# >
# >=
# ==
# !=

# The if statement

# temp = 15
# if temp > 30:
#     print("it is hot")
# elif temp < 10:
#     print("it is cold")
# else:
#     print("it is OK")

# print ('done')
# The following is a good example of turnary operators
# where an if statement can be combined and written on one line
# age = 22
# message = "Eligble" if age >= 18 else "not eligible"
# print (message)

# now lets look at the
# and
# or
# not

# hig_income = True
# good_credit = False

# if (hig_income and good_credit):
#     print ("elegible")
# else:
#     print ("not eligible")

# Chaining operators

# age = 10
# if 18 <= age < 65:
#     print("he is eligible")
# else:
#     print("he is not eligible")

# the for loop

# for number in range(3):
#     print (f"tryin to reach you for the {number+1} time")

# Funtions
# def greet(first_name, last_name):
#     print(f"welcom {first_name} {last_name}")

# greet("joseph", "mousa")


# def get_greeting(name):
#     return (f"Hi {name}")

# message = get_greeting("joe")

# file = open("content.txt", "w")
# file.write(message)


# creating a function that accept a varialbe number of parameters

# def multiply (*numbers):
#     total = 1
#     for number in numbers:
#         total = total *number
#     return total

# print (multiply(2, 3, 5))


# another twist on functions (a dictionary)

# def save_user(**user):
#     print(user)
#     print (user["name"])



# save_user(id=1, name="john", age=22)

