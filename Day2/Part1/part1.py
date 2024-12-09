def read_input(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

def is_safe_report(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(file_path):
    reports = read_input(file_path)
    safe_count = sum(is_safe_report(report) for report in reports)
    return safe_count

def main():
    safe_count_small = count_safe_reports('input/small')
    print(f'Number of safe reports in small.txt: {safe_count_small}')

    safe_count_input = count_safe_reports('input/input.txt')
    print(f'Number of safe reports in input.txt: {safe_count_input}')

if __name__ == "__main__":
    main()
