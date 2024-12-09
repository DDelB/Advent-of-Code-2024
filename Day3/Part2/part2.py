import re

def extract_and_multiply(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    total_sum = 0
    mul_enabled = True

    for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        if do or dont:
            mul_enabled = bool(do)
        else:
            product = int(a) * int(b)
            total_sum += product * mul_enabled

    return total_sum

file_path = 'input/input.txt'
result = extract_and_multiply(file_path)
print(f"The total sum of all enabled multiplications is: {result}")

file_path = 'input/small'
result = extract_and_multiply(file_path)
print(f"The total sum of all enabled multiplications is: {result}")

