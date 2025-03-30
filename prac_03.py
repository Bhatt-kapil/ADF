
def calc():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
 
calc()
choice = input("Enter the number corresponding to the operation: ")
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
   
if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
elif choice == '4' and num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
elif choice == '4' and num2 == 0:
        print("Error: Division by zero is not allowed.")
else:
        print("Invalid input! Please select a valid operation.")


