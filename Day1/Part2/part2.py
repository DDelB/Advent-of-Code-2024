from collections import Counter

def read_input(file_path):
    left_column = []
    right_column = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_column.append(left)
            right_column.append(right)
    return left_column, right_column

def calculate_similarity_score(left_column, right_column):
    right_count = Counter(right_column)
    similarity_score = sum(left * right_count[left] for left in left_column)
    return similarity_score

def main():
    left_list, right_list = read_input('input/small.txt')
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f'Similarity score for small.txt: {similarity_score}')

    left_list, right_list = read_input('input/input.txt')
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f'Similarity score for input.txt: {similarity_score}')

if __name__ == "__main__":
    main()
