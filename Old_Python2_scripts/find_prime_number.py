import math
from math import sqrt; 
from itertools import count, islice


num = int(input("Please enter an integer: "))


def is_Prime(num):
    return all(num%i for i in islice(count(2), int(sqrt(num)-1)))
    
def main():
	
    if is_Prime(num):
        print (num, "is a prime number")
    else:
        print (num, "is not a prime number")
main()




