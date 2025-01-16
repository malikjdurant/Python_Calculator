def calculation(first_num, second_num, operation):
    if operation == "+":
        return f"Here is your result: {first_num + second_num}"

    elif operation == "-":
        return f"Here is your result: {first_num - second_num}"

    elif operation == "*":
        return f"Here is your result: {first_num * second_num}"

    else:
        return f"Here is your result: {int(first_num / second_num)}"

print("Enter your first number: ")
num1 = int(input())

print("Enter your second number: ")
num2 = int(input())

print("Enter your operation: ")
op = input()

print(calculation(num1, num2, op))