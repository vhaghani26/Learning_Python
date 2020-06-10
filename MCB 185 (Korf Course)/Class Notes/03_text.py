#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code

"""

# Variables with text are called strings

s = 'ACGT' # a string

# Square brackets let you access sub-strings as 'slices'
# Follow closely below, because the endpoints can be confusing
# The first number before : is the starting index
# The second number : is one larger than the last index

print(s, s[0], s[1])
print(s[2], s[2:3], s[2:4], s[2:5])

# You can also do the following shortcuts

print(s[:2]) # the 0 is implict on the left
print(s[2:]) # the end of the string is implicit on the right

# The + operator concatenates strings

s = s + 'N'
s += 'n'   # note that += is a shorthand for s = s +, just like in math
print(s)

# The * operator repeats strings

s *= 3
print(s)

# The len() function returns the length of a string
# Some function like len() return values, others like print() do not

print(len(s))

"""
