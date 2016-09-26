# Welcome to Bad Python Lessons, Lesson 1.
# All lessons are written so you can run them in an interpreter without any errors
# We will not walk you through getting an interpreter running.


# This version of Python is 3.5

# First let's start with variables, in algebra you will know `x`.
# So let's make a variable called x, and assign it a value of 5

x = 5

# In math, a plain equal sign (`=`) usually means is equivilant to, but at least in python you are assigning `x` to a value of `5`
# not just stating that x is equivilant to 5, it is 5.

# You may have an equation that looks like this
# y = x * 2

# We can accomplish that with this:

def y (x):
    return x * 2
    
# You use the def keyword to define a function, which will be reffered to as the word immedietly after the `def` keyword. In this case it is `y`
# You then state the required inputs, in this case `x`, and then inside the function, which you can tell what is and isn't in the function
# thanks to the whitespace, the function `returns` x multiplied by two.

# so y(2) has a value/returns 4
