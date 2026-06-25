while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", num1 + num2)
    elif choice == "2":
        print("Result =", num1 - num2)
    elif choice == "3":
        print("Result =", num1 * num2)
    elif choice == "4":
        print("Result =", num1 / num2)