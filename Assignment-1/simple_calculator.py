def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    return a/b
def modulus(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    return a%b


def main():
    while True:
        print("\n Simple Calculator|| Choose a Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divide ")
        print("5. Modulus")
        print("6. Exit the app ")
        choice=input("Enter your choice: ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a valid option (1-5).")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid number format. Please enter numeric values.")
            continue
        if choice == '1':
            result = addition(a, b)
            print(f"{a} + {b} = {result}")
        
        elif choice == '2':
            result = subtraction(a, b)
            print(f"{a} - {b} = {result}")
        
        elif choice == '3':
            result = multiplication(a, b)
            print(f"{a} * {b} = {result}")
        
        elif choice == '4':
            result = division(a, b)
            print(f"{a} / {b} = {result}")
        
        elif choice == '5':
            result = modulus(a, b)
            print(f"{a} % {b} = {result}")
if __name__ == "__main__":
    main()