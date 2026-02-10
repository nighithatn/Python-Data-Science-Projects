from circle import area_circle
from rectangle import area_rectangle
from triangle import area_triangle

def main():
    while True:
        print("\n--- Math Shapes Calculator ---")
        print("1. Area of Circle")
        print("2. Area of Rectangle")
        print("3. Area of Triangle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            r = float(input("Enter radius: "))
            print("Area of Circle:", area_circle(r))

        elif choice == '2':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Area of Rectangle:", area_rectangle(l, w))

        elif choice == '3':
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of Triangle:", area_triangle(b, h))

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
