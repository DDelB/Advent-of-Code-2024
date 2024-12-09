import re

def extract_and_multiply(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.findall(pattern, data)

    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum

file_path = 'input/input.txt'
result = extract_and_multiply(file_path)
print(f"The total sum of all valid multiplications is: {result}")

file_path = 'input/small'
result = extract_and_multiply(file_path)
print(f"The total sum of all valid multiplications is: {result}")

