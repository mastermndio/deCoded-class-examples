# Print out numbers 1 to 100
# For numbers that are evenly divisible by 3 print the word "Fizz" instead of the number
# For numbers that are evenly divisible by 5 print the word "Buzz" instead of the number
# For numbers that are evenly divisible by 3 and 5 print the word "FizzBuzz" instead of the number

for number in range(101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    else:
        print(number)
