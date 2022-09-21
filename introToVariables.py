x = 3  # int
y = "this is a string"  # string
z = 1.3  # float
print("hello, these are some basic variables: ")
# notice how we "cast" the numeric variables to string when printing them!
# in this case, we're asking the program to treat the numeric variables as if they were strings! The reason why is that python cannot understand print commands that contain multiple types of datatypes
print(str(x) + " is an int!")
print(type(x))
print(y + "   <-- that was a string!")
print(type(y))
print(str(z) + " is a float!")
print(type(z))
