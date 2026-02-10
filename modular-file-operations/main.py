from word_count import count_words
from line_count import count_lines
from char_count import count_characters

def main():
    filename = input("Enter the file name (with extension): ")

    while True:
        print("\n--- File Operations Menu ---")
        print("1. Count Words")
        print("2. Count Lines")
        print("3. Count Characters")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == '1':
                print("Word count:", count_words(filename))

            elif choice == '2':
                print("Line count:", count_lines(filename))

            elif choice == '3':
                print("Character count:", count_characters(filename))

            elif choice == '4':
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice! Try again.")

        except FileNotFoundError:
            print("Error: File not found.")
            break

if __name__ == "__main__":
    main()
