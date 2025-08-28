
num1 = int(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number : "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero." 
else:
    result = "Invalid operator!"    


print((num1), (op), (num2), '=', (result))
# Simple calculator program with user interaction


