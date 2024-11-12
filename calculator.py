ch="y"
while ch.lower()=="y":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter the operation number (1/2/3/4): ")
    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
        operation = "Division"
    else:
        result = "Invalid operation choice."

    print(operation, "result:", result)
    ch=input("Press y to continue, else press any other key to exit: ")
else:
    print("Thank you for using the calculator :)")
