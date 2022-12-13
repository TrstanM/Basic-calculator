# Author: Tristan Miller
# Program start-up
print("Welcome To the Calculator!\n")
print("What would you like to use")
method = input("+, -, /, *: ")

# Loop & Selection Statements
if method == "+":
    n1= input("Enter First number:")
    n2 = input("Enter Second number:")
    sum = float(n1) + float(n2)
    print("The sum of {0} and {1} is {2}" .format(n1, n2, sum))
elif method == "-":
    n1 = input("Enter First number:")
    n2 = input("Enter Second number:")
    sum = float(n1) - float(n2)
    print("The difference of {0} and {1} is {2}" .format(n1, n2, sum))
elif method == "/":
    n1 = input("Enter First number:")
    n2 = input("Enter Second number:")
    sum = float(n1) / float(n2)
    print("The quotient of {0} and {1} is {2}" .format(n1, n2, sum))
elif method == "*":
    n1 = input("Enter First number:")
    n2 = input("Enter Second number:")
    sum = float(n1) * float(n2)
    print("The product of {0} and {1} is {2}" .format(n1, n2, sum))
else:
    print("That's not a number silly")

# lists
string_list = ["Hello", "Hi", "Howdy"]
int_list = [1,2,3]
mixed_list = ["hi", 2.345, 3]

# dictionary
my_dict = {"Name": "Tristan", "Age":"26", "Location":"Santa Clarita"}
