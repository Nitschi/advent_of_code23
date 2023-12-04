from util.read_text import get_input_lines

result = 0
for line in get_input_lines(1):
    for c in line:
        if c.isnumeric():
            number = int(c)*10
            break
    for c in reversed(line):
        if c.isnumeric():
            number += int(c)
            break
    result += number

print(result)