"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_equation = input("Enter an equation > ")
    tokens = user_equation.split(" ")
    if tokens[0] == 'q':
        print("Quit.")
        break
    else:
        math_expression = tokens[0]
        num1 = float(tokens[1])
        if len(tokens) == 3:
            num2 = float(tokens[2])

        answer = ""

        if math_expression == "+":
            answer = add(num1, num2)
        elif math_expression == "-":
            answer = subtract(num1, num2)
        else:
            print("That was not a math expression.")

        print(answer)

