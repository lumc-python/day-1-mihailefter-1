# Exercise 5: Dictionaries
# ==========
#
# We are going to store the output of a function (f(x)=x2) together with its
# input in a dictionary.
# - Make a dictionary containing all squares smaller than 100.
# - Print the content of this dictionary in english, e.g.,"4 is the square of 2".

d = {}

for i in range(10):
    d[i] = i ** 2

for k in d:
    print(f"{d[k]} is the square of {k}")
