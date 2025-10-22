# calculator.py

# --- Define functions for each operation ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

# --- Main Program ---
def main():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("⚠️ Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
