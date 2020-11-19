#print ("Ebenezer")
#print ("Fresh Boy")

school = "Kwame Nkrumah University of Science and Technology"

print (school)
# lenght of string
print (len(school))
 #writing a string on multiple lines
 # use 3 double quotes

schoolStatement = """
My first school is called 
Kwame Nkrumah University of Science and Technology
"""
print (schoolStatement)

# we can use /n to go to a new line in a bulk sentence

#strings in python already behaves like an array. so we can get specific characters in a string by the use of indexes
#this will print out the first letter
print(school[0]) 
#we can give it a range of characters too
#this will print from the first character to the 6th character
print (school[0:6])
#this will print out the whole string
print(school[0:])
#we can use negation or minus to start the ranging from the last character
print (school[-3:])
#this will print the last character in the string
print (school[-1])


#converting uppercase
print (school.upper())

#converting to lowercase
print (school.lower())

#converting only the first letter of each word
print (school.title())


#replacing words or characters in a string
print (school.replace('Nkrum', 'Nku'))