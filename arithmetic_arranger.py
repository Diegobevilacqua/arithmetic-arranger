import re

def arithmetic_arranger(problems, display_answers = False):
  if (len(problems) > 5):
    return 'Error: Too many problems.'

  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''

  for problem in problems:
    first_operand = problem.split(' ')[0]
    operator = problem.split(' ')[1]
    second_operand = problem.split(' ')[2]

    if (re.search('\D', first_operand) or re.search('\D', second_operand)):
      return 'Error: Numbers must only contain digits.'

    if (operator != '+' and operator != '-'):
      return "Error: Operator must be '+' or '-'."

    if (int(first_operand) > 9999 or int(first_operand) < -9999 or int(second_operand) > 9999 or int(second_operand) < -9999):
      return 'Error: Numbers cannot be more than four digits.'

    length = max(len(first_operand), len(second_operand)) + 2
    first_line += ''.join([' ' for _ in range(length - len(first_operand))]) + first_operand + '    '

    if (len(first_operand) <= len(second_operand)):
      
      space = ' '
    else:
      space = ''.join([' ' for _ in range(length - len(second_operand) - 1)])

    second_line += (operator + space + second_operand).ljust(length + 4)
    third_line += ''.join(['-' for _ in range(length)]).ljust(length + 4)

    result = ''

    if (display_answers):
      if (operator == '+'):
        result = str(int(first_operand) + int(second_operand))
      else:
        result = str(int(first_operand) - int(second_operand))

    # fourth_line += ''.join([' ' for _ in range(length - len(result))]) + result.ljust(length + 4)
    fourth_line += ''.join([' ' for _ in range(length - len(result))]) + result + '    '
    ret = first_line + '\n' + second_line + '\n' + third_line

    if (fourth_line != ''):
      ret += '\n' + fourth_line

  return ret
