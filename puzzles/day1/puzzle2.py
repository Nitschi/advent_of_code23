from util.read_text import get_input_lines
NUMBERS = tuple(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [f"{n}" for n in range(10)])

def is_number(i: int, line: str) -> bool:   
    if line.startswith(NUMBERS, i):
        return True
    
def to_int(s: str) -> int:
    if s[0].isnumeric():
        return int(s[0])
    
    for i, number in enumerate(NUMBERS):
        if s.startswith(number):
            return i


result = 0
for line in get_input_lines(1):
    for i in range(len(line)):
        if is_number(i, line):
            number = to_int(line[i:])*10
            break
    for i in reversed(range(len(line))):
        if is_number(i, line):
            number += to_int(line[i:])
            break
    result += number

print(result)

