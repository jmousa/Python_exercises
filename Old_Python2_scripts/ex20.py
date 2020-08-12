from sys import argv

script, data_file = argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print (line_count, f.readline())

input_file = open(data_file)

print ("First let's print the whole file:\n")
print_all(input_file)

print ("Now let's rewind, kind of like a tape.")
rewind(input_file)

print ("Let's print three lines:")
print_a_line(1, input_file)
print_a_line(2, input_file)
print_a_line(3, input_file)

