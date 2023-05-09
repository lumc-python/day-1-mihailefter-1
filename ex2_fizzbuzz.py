# Exercise 3: FizzBuzz
# ==========
#
# Write a program that prints the numbers from 1 to 100. But for multiples of
# `3` print `Fizz` instead of the number and for the multiples of` 5` print
# `Buzz`. For numbers which are multiples of both `3` and `5` print `FizzBuzz`.

# Longer version
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Shorter version
for i in ['Fizz' * (i % 3 < 1) + 'Buzz' * (i % 5 < 1) or i for i in range(1, 101)]:
    print(i)
