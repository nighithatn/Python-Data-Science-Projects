from uppercase import to_uppercase
from lowercase import to_lowercase
from reverse import reverse_string

def main():
    while True:
        print("\n--- String Processor Menu ---")
        print("1. Convert to Uppercase")
        print("2. Convert to Lowercase")
        print("3. Reverse the String")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting program. Bye!")
            break

        text = input("Enter a string: ")

        if choice == '1':
            print("Result:", to_uppercase(text))
        elif choice == '2':
            print("Result:", to_lowercase(text))
        elif choice == '3':
            print("Result:", reverse_string(text))
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

