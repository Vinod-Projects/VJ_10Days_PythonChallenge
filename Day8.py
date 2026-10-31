#Functions

def greet(name):
    print("Welcome to Lazy Learners: {name}")

greet("Vinod")

'''
To return a action inside the function mention return inside the function
'''
def add(a,b):
    return a+b

print(add(10,20))
print(add(300,400))

'''
Sample Calculator 
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

first_number = float(input("Enter the first number: "))
operator = input("Choose an operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = add(first_number, second_number)
elif operator == "-":
    result = subtract(first_number, second_number)
elif operator == "*":
    result = multiply(first_number, second_number)
elif operator == "/":
    try:
        result = divide(first_number, second_number)
    except ValueError as error:
        print(error)
else:
    print("Invalid operation.")

if operator in {"+", "-", "*"} or (operator == "/" and second_number != 0):
    print("Result:", result)
