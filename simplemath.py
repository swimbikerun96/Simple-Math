def simpleMath(firstNumber, secondNumber):
    try:
        n1 = int(firstNumber)
        if n1 < 0:
            return "Cannot Enter a Negative Number"
        n2 = int(secondNumber)
        if n2 < 0:
            return "Cannot Enter a Negative Number"
        add = n1 + n2
        multiply = n1 * n2
        subtract = n1 - n2
        divide = n1 / n2
        return f"{n1} + {n2} = {add}\n{n1} x {n2} = {multiply}\n{n1} - {n2} = {subtract}\n{n1} / {n2} = {divide}"
    except ValueError:
        return "Please Enter Numbers"
    except ZeroDivisionError:
        return "Make Sure the Second Number is NOT Zero!"
