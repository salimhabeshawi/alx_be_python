def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == o:
                return "Division by zero cannot be performed"
            else:
                return num1 / num2
        case _:
            return "you entered an invalid operator"