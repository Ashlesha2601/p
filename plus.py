import sys


if len(sys.argv) < 3:
    print("Please provide two numbers as arguments.")
    sys.exit(1)


num1 = float(sys.argv[1])
num2 = float(sys.argv[2])


result = num1 + num2


print("The sum of", num1, "and", num2, "is:", result)

