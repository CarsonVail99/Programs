def questions():
    number1 = int(input("Enter the first number: "))
    operator = input("Enter the operator: \n+, -, *, /")
    number2 = int(input("Enter the second number: "))
    return number1, number2, operator


def calculation(number1, number2, operator):
    try:
        if operator == "+":
            print(f'{number1} + {number2} = {number1 + number2}')
        elif operator == "-":
            print(f'{number1} - {number2} = {number1 - number2}')
        elif operator == "*":
            print(f'{number1} * {number2} = {number1 * number2}')
        elif operator == "/":
            print(f'{number1} / {number2} = {number1 / number2}')
        else:
            print("Invalid operator")
            return calculation(number1, number2, operator)
    except ZeroDivisionError:
        print(f"Can't divide {number1}by {number2}")


def main():
    calculation(*questions())
if __name__ == "__main__":
    main()


