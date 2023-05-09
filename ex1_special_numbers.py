# Exercise 1: Special numbers
# ==========
#
# Print all the numbers between `10` and `1313` (both included) which are
# divisible by `13` and multiple of `5`.

for number in range(10, 1314):
    if number % 13 == 0 and number % 5 == 0:
        print(number)
