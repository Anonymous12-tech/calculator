#Making a calculator in python

#User input
num1 = int(input("Enter number: "))
num2 = int(input("Enter 2nd number: "))


#Functions
def add(num1, num2):
    return num1 + num2

def subtract(num, num2):
    return num - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


#If satements
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
operator = input("Which operator do you want to use: ")
if operator == "1":
    print(add(num1, num2))

elif operator == "2":
    print(subtract(num1, num2))

elif operator == "3":
    print(multiply(num1, num2))

elif operator == "4":
    print(divide(num1, num2))