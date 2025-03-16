# Function to perform the mathematical operation
def calculator():
    # Taking user input for the numbers and the operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on the user's input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Invalid operation. Please choose from +, -, *, or /."

    return f"The result of {num1} {operation} {num2} = {result}"

# Call the calculator function
print(calculator())
