operator = input("Enter an operator: ")
rounded = input("Would you like the number to be rounded to 1 decimal place?: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+" and rounded == "No":
    result = num1 + num2
    print(result)
elif operator == "-" and rounded == "No":
    result = num1 - num2
    print(result)
elif operator == "*" and rounded == "No":
    result = num1 * num2
    print(result)
elif operator == "/" and rounded == "No":
    result = num1 / num2
    print(result)
elif operator == "+" and rounded == "Yes":
    result = num1 + num2
    print(round(result))
elif operator == "-" and rounded == "Yes":
    result = num1 - num2
    print(round(result))
elif operator == "*" and rounded == "Yes":
    result = num1 * num2
    print(round(result))
elif operator == "/" and rounded == "Yes":
    result = num1 / num2
    print(round(result))