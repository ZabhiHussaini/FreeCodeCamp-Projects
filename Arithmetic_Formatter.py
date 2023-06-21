problems = input()
def arrange_problems(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    line1 = line2 = line3 = line4 = ""

    for i, problem in enumerate(problems):
        operands = problem.split()
        if len(operands) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        width = max(len(operand1), len(operand2))
        answer = str(int(operand1) + int(operand2)) if operator == '+' else str(int(operand1) - int(operand2))

        line1 += operand1.rjust(width + 2)
        line2 += operator + " " + operand2.rjust(width)
        line3 += "-" * (width + 2)
        if show_answers:
            line4 += answer.rjust(width + 2)

        if i < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            if show_answers:
                line4 += "    "

    arranged_problems.append(line1)
    arranged_problems.append(line2)
    arranged_problems.append(line3)
    if show_answers:
        arranged_problems.append(line4)

    return "\n".join(arranged_problems)