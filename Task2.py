# simple_calculator
import json;

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    operations = {
        '1': 'Add',
        '2': 'Subtract',
        '3': 'Multiply',
        '4': 'Divide'
    }
    for key, value in operations.items():
        print(f"{key}. {value}")
    while True:
        choice = input("Choose an operation (1/2/3/4): ")
        if choice in operations:
            return choice
        print("Invalid choice. Please choose a valid operation.")

def main():
    print("Simple Calculator")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
