"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_equation = input("Enter an equation > ")
    tokens = user_equation.split("")
    if tokens[0] == 'q':
        print("Quit.")
        break
    else:
        function = tokens[0]
        num1 = tokens[1]
        if len(tokens) == 3:
            num2 = tokens[2]

