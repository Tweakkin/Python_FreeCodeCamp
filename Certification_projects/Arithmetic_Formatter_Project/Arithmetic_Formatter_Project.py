def arithmetic_arranger(problems, show_answers=False):
    first_line = []
    second_line = []
    lines = []
    last_line = []

	#Checking the number of problems
    if len(problems)>5:
        return "Error: Too many problems."

	#A loop that handles each variable in the list
    for operation in problems:
        first_number = ""
        second_number = ""
        operator = ""
        flag = 0
		#A loop that handles each character in the operation
        for char in operation:
            if char == '*' or char == '/':
                return "Error: Operator must be '+' or '-'."
            elif char != " " and char != '+' and char != '-' and flag == 0:
                first_number += char
            elif char == " ":
                continue
            elif char == '+' or char == '-':
                flag = 1
                operator = char
            elif char != " " and char != '+' and char != '-' and flag == 1:
                second_number += char
		
		#Handling errors
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
		
		#Handling errors	
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

		#Filling up the lists	
        width = max(len(first_number), len(second_number)) + 2
        first_line.append(first_number.rjust(width))
        second_line.append(operator + second_number.rjust(width - 1))
        lines.append('-'*width)
        if show_answers:
            if operator == '+':
                answer = int(first_number) + int(second_number)
            elif operator == '-':
                answer = int(first_number) - int(second_number)
            last_line.append(str(answer).rjust(width))
        
    #Converting the lists to strings and seperating them with spaces    
    first_line = '    '.join(first_line)
    second_line = '    '.join(second_line)
    lines = '    '.join(lines)

	#Returning the results
    if show_answers:
        last_line = '    '.join(last_line)
        return first_line + '\n' +second_line + '\n' + lines + '\n' + last_line
	else:
    	return first_line + '\n' +second_line + '\n' + lines
