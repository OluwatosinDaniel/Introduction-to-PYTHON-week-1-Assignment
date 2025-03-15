def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))  # Convert input to float
    num2 = float(input("Enter the second number: "))  # Convert input to float
    operation = input("Enter the operation (+, -, *, /): ").strip()  # Remove extra spaces

    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

# Run the calculator
calculator()
