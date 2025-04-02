def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add")
    print("2. Divide")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Modulus")
    print("6. Exponential")
    print("7. FloorDiv")
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    
    elif choice == '2':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero ")
    
    elif choice == '3':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    
    elif choice == '4':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    
    elif choice == '5':
        print(f"Result: {num1} % {num2} = {num1 % num2}")
    
    elif choice == '6':
        print(f"Result: {num1} ^ {num2} = {num1 ** num2}")
    
    elif choice == '7':
        print(f"Result: {num1} // {num2} = {num1 // num2}")
    
    else:
        print("Invalid input. Please select a valid operation.")

calculator()
