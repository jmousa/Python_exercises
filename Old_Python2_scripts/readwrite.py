#str = input("Enter your input: ");
#print ("Received input is : ", str)
 
#=======================================

fh = open("c:/Users/Lubana/Desktop/data.txt", "w")		# Open the text file data for writing
fh.write("Python is a great language.\n");

fh.close()		# Close opend file

#=======================================

fh = open("c:/Users/Lubana/Desktop/data.txt", "r")		# Open the text file data for reading
str = fh.read();
print ("Read String is\n",str)

fh.close()		# Close opend file

#=======================================
