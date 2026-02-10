
"""
Main Calculator Program
This program integrates multiple operation modules (addition, subtraction,
multiplication, division) and allows user to perform calculations.
"""

# Importing operation modules
import NumberAddition
import NumberSubstraction
import NumberMultiplication
import NumberDivision
1
# Function Name: StartCalculator
# Description: Provides a menu-driven calculator using imported modules.
# Parameters: None
# Return: None
def StartCalculator():
    while True:
        print("\n=== Python Modular Calculator ===")
        print("1. NumberAddition")
        print("2. NumberSubtraction")
        print("3. NumberMultiplication")
        print("4. NumberDivision")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting Calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = NumberAddition.PerformAddition(num1, num2)
                print(f"Result: {result}")

            elif choice == "2":
                result = NumberSubtraction.PerformSubtraction(num1, num2)
                print(f"Result: {result}")

            elif choice == "3":
                result = NumberMultiplication.PerformMultiplication(num1, num2)
                print(f"Result: {result}")

            elif choice == "4":
                result = NumberDivision.PerformDivision(num1, num2)
                print(f"Result: {result}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


# Program entry point
if __name__ == "__main__":
    StartCalculator()

