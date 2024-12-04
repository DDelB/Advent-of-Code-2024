def read_input(file_path):
    left_column = []
    right_column = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_column.append(left)
            right_column.append(right)
    return left_column, right_column

def calculate_total_distance(left_column, right_column):
    left_column.sort()
    right_column.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_column, right_column))
    return total_distance

def main():
    # Test with small.txt
    left_list, right_list = read_input('input/small.txt')
    total_distance = calculate_total_distance(left_list, right_list)
    print(f'Total distance for small.txt: {total_distance}')

    # Test with input.txt
    left_list, right_list = read_input('input/input.txt')
    total_distance = calculate_total_distance(left_list, right_list)
    print(f'Total distance for input.txt: {total_distance}')

if __name__ == "__main__":
    main()
