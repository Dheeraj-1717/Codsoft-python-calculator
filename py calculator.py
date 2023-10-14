def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        choice = input("Enter your choice: ")

        if choice == "quit":
            break

        if choice in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "add":
                    print("Result:", add(num1, num2))
                elif choice == "subtract":
                    print("Result:", subtract(num1, num2))
                elif choice == "multiply":
                    print("Result:", multiply(num1, num2))
                elif choice == "divide":
                    result = divide(num1, num2)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print("Result:", result)
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Invalid choice. Please enter a valid operation.")

if __name__ == "__main__":
    calculator()
