def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return (a+b)

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return (a-b)
    
def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return (a * b)
   
def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return (a/b)


print ("Let's do some math with just functions!")


value1 = int(input("enter the first number\n"))
value2 = int(input("enter the first number\n"))

age = add(value1, value2)
height = subtract(value1, value2)
weight = multiply(value1, value2)
iq = divide(value1, value2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")



age = float (input("how old are you\n"))
height = float (input("how tall are you\n"))
weight = float (input("How much do you weigh?\n"))

print ("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
