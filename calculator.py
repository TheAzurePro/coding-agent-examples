# Simple Calculator

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Select operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        print(f"The Sum of given 2 numbers is {result}")
    elif choice == '2':
        result = num2 - num1
        print(f"The Result of subtracting 1st number from 2nd is {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The Product of given 2 numbers is {result}")
    elif choice == '4':
        if num2 == 0:
            print("Division not possible")
        else:
            result = num1 / num2
            print(f"The Division of 1st number with given 2nd number is {result}")
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()
