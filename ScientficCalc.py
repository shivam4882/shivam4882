import math

def main():
    print("Full-Featured Scientific Calculator")
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'sqrt' for square root")
        print("Enter 'sin' for sine function")
        print("Enter 'cos' for cosine function")
        print("Enter 'tan' for tangent function")
        print("Enter 'log' for logarithm")
        print("Enter 'exp' for exponential")
        print("Enter 'quit' to exit")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ["add", "sub", "mul", "div"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if user_input == "add":
                result = num1 + num2
            elif user_input == "sub":
                result = num1 - num2
            elif user_input == "mul":
                result = num1 * num2
            elif user_input == "div":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Division by zero is not allowed.")
                    continue
        elif user_input in ["sqrt", "sin", "cos", "tan"]:
            num = float(input("Enter a number: "))
            if user_input == "sqrt":
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    print("Square root of a negative number is not allowed.")
                    continue
            elif user_input == "sin":
                result = math.sin(num)
            elif user_input == "cos":
                result = math.cos(num)
            elif user_input == "tan":
                result = math.tan(num)
        elif user_input == "log":
            num = float(input("Enter a number: "))
            if num > 0:
                result = math.log(num)
            else:
                print("Logarithm of a non-positive number is not allowed.")
                continue
        elif user_input == "exp":
            num = float(input("Enter a number: "))
            result = math.exp(num)
        else:
            print("Invalid input. Please try again.")
            continue

        print("Result: " + str(result))

if __name__ == "__main__":
  main()