def arithmetic_arranger(problems, show_answers=False):
    # Error checking
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_numbers = []
    second_lines = []
    dash_lines = []
    answers = []
    
    for operation in problems:
        first_number = ""
        second_number = ""
        operator = ""
        flag = 0
        
        for char in operation:
            if (char != " " and char != '+' and char != '-' and flag == 0):
                first_number += char
            elif (char == "+" or char == '-'):
                operator = char
                flag = 1
            elif (char == '*' or char == '/'):
                return "Error: Operator must be '+' or '-'."
            elif (flag == 1 and char != " "):
                second_number += char
        
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(first_number), len(second_number) + 2) + 2
        
        first_numbers.append(first_number.rjust(width))
        second_lines.append(operator + second_number.rjust(width - 1))
        dash_lines.append('-' * width)
        
        if show_answers:
            if operator == '+':
                answer = int(first_number) + int(second_number)
            else:
                answer = int(first_number) - int(second_number)
            answers.append(str(answer).rjust(width))
    
    first_line = '    '.join(first_numbers)
    second_line = '    '.join(second_lines)
    dash_line = '    '.join(dash_lines)
    
    if show_answers:
        answer_line = '    '.join(answers)
        return first_line + '\n' + second_line + '\n' + dash_line + '\n' + answer_line
    else:
        return first_line + '\n' + second_line + '\n' + dash_line