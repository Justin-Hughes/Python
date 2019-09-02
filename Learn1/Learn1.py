import sys
import math
import random
import threading
import time
from functools import reduce

print("Hello World")
name = input("What is your name?  ")
print("Hi", name)

v1 = ( # parentheses can be spread across multiple lines
    1+2
    +3
)

#backslash allows for multi line function without parentheses
v1 = 1 + 2 \
    + 3

# semi colons allow for declaring multiple variables on the same line
v1 = 5; v5 = 3

# data types are dynamic and can change, all data types are objects
print(type(v1))
print(sys.maxsize)
print(sys.float_info.max) #only accurate to 15 digits
f1 = 1.1111111111111111 #proof of innaccuracy
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# complex numbers = real part + imaginary
comnum1 = 5 + 6j

str1 = "Escape Sequence \' single quotes \" double quotes \t tab character \\ backslash \n new line"
str2 = ''' Triple quoted ' " '''

print(str2)

print(6, 2, 1993, sep='/') # sep provides the means of seperating printed items
print("No new line", end='') # end provides the means of specifying the action taken at the end of the line
#print("\n %04d %s $.2f" % (1, "Justin", 1.234)) # string formatting DOES NOT
                            #WORK WITH GIVEN EXAMPLE, FIND RESOURCE TO LEARN
print("5 ^ 2 =", 5 ** 2)
print("5 / 2 =", 5 / 2) # normal division
print("5 // 2 =", 5 // 2) # integer division

# math has a lot of built in math functions
print("Random int = ", random.randint(1, 101))

print(math.inf > 0)

print(math.inf - math.inf) # NaN not a number



# Conditionals
age = 15

if age > 21:
    print("You can drive a tractor")
elif age >= 16:
    print("You can drive a car")
else:
    print("you ")


if age < 5:
    print("Stay Home")
elif(age >= 5) and (age <= 6):
    print("Grade %d", (age - 5))
else:
    print("College")

# condition_true if condition else condition_false Turnary operator ( ?: in C#)
canVote = True if age >= 18 else False

# Strings
print(r"I'll be ignored \n") # the r modifier for strings ignores escape sequences
print("Hello " + "You") # concatenate with +
str3 = "Hello You"

print("Length ", len(str3)) # len gets the length of the string
print("First ", str3[0]) # Prints the first character of the string
print("Last ", str3[-1]) # Prints the last character of the string
print("First three ", str3[0 : 3]) # Prints a range of the string, not including the range limit
print("Every other ", str3[0 : -1 : 2]) # Selects the entire range of the string (0 as the beginning -1 as the end)
                                        # and prints every second element (2) (Known as slicing, [start:end:step])
str3 = str3.replace("Hello", "Goodbye") # replace(x, y) replaces every x with y
print(str3)

str3 = str3[:8] + 'y' + str3[9:] # [:8] selects from beginning to the eigth index, + 'y' adds y, [9:] selects
                                 # from the ninth index to the end
print(str3)

print("you" in str3) # checks if string "you" is in str3 and returns a bool
print("you" not in str3) # checks if string "you" is not in str3 and returns a bool
print("You index", str3.find("you")) # Finds index of first occurence of "you" if no occurence is found it returns -1
print("    Hello      ".strip())# Trims whitespace
print("    Hello      ".lstrip())# Trims whitespace from left side
print("    Hello      ".rstrip())# Trims whitespace from right side
print(" ".join(["Some", "Words"])) # joins the selected string on a list, in this case it adds spaces to the list
                                   # items
print("A string".split(", ")) # split() converts strings to lists with the delimeter as an optional
                              # parameter
int1 = int2 = 5

print(f'{int1} + {int2} = {int1 + int2}') # f is the string interpolation character for python.  $ in C#
print("A String".lower())# converts all characters to lowercase
print("A String".upper())# converts all characters to UPPERCASE
print("AString123".isalnum()) # .isalnum checks whether or not a string contains only alpha numeric characters (spaces do not count as alpha numeric)
print("AString".isalpha()) # Checks whether or not a string contains only letters
print("123".isdigit()) # Checks whether or not a string contains only numbers


# l1sts 
# Mutable - can be changed; Immutable - cannot be changed
# Extended Slicing (explains ::-1 collection reversing) https://docs.python.org/2.3/whatsnew/section-slices.html

l1 = [1, 3.14, "Justin", True] # There are no type l1mitations for l1sts in Python
print("Length", len(l1)) # Prints the length of the l1st
print("First", l1[0]) # Prints the first element of the l1st
print("Last", l1[-1]) # Prints the last element of the l1st
print("First three", l1[0 : 3]) # Prints a range of the l1st, not including the range l1mit
print("Every other", l1[0 : -1 : 2]) # Selects the entire range of the l1st (0 as the beginning -1 as the end)
                                        # and prints every second element (2) (Known as slicing, [start:end:step])

l1[0] = 2 # Unl1ke with strings you can directly change l1sts using index values.
l1[2:4] = ["Bob", False] # You can change multiple elements at the same time with Python. Just to reiterate; the range [startIndex, endIndex] includes the startIndex but not the endIndex
l1[2:2] = ["Paul", 9] # Inserts at index without deleting (first element being added will now have that index value)
#l1.insert(2, "Paul") # Alternative to above but can only add one element
l2 = l1 + ["Egg", "Paul", 4]
l2.remove("Paul") # Removes first instance of selected element
l2.pop(0) # Removes at an index
print(l1, l2)
l2 = ["Bacon", 5] + l2 # Adds to the beginning of the l1st
l3 = [[1, 2], [3, 4]] # Multi Dimensional Arrays
print("[1,1]", l3[1][1])

print("1" in l1) # checks if element "1" is in l1 and returns a bool
print("1" not in l1) # checks if element "1" is not in l1 and returns a bool

li = [1, 3, 6, 15, 7132, 52, 1, 9, -2]
print (min(li)) # Prints the min value from a list, the list must be of one type though
print (max(li)) # Prints the max value from a list, same rule
print(li[::-1]) # Reverses a list using Extended Slicing


# Loops 

w1 = 1 # index must be defined outside of while loop

while w1 < 5:
    print(w1)
    w1 += 1

w2 = 0
while w2 <= 20:
    if w2  % 2 == 0:
        print(w2)
    elif w2 == 9:
        break # breaks out of current loop
    elif w2 == 7:
        w2 += 1
        continue # Skips to the next cycle of the loop without running the rest of the code in the loop
    w2 += 1

l4 = [1, 3.14, "Justin"]

w3 = 0
while len(l4) > w3:
    print(l4[w3])
    w3 += 1


for x in range(0, 21): # Does not include 21
    print(x, ' ', end="")
print()

l5 = range(1, 21)

for x in l5:
    print()
    print(x, ('  ' * x), x)

#y = 2
#while y != True:
#    time.sleep(1)
#    print(y)
#    y *= y


#Iterator
#Passes a list to iter which allows you to cycle through that list via next(iter_name)
#(Don't forget that you can put functions in lists in python)

l6 = range (0, 11) # does not include 11
itr = iter(l6)
print(next(itr)) # prints next item(number 0) from the list (l6) loaded into the iter (itr)
print(next(itr)) # prints next item(number 1) from the list (l6) loaded into the iter (itr)
# Throws StopIteration error if there is no next item
