def read_input(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

def is_safe_report(report):
    def is_increasing_or_decreasing(r):
        increasing = all(1 <= r[i+1] - r[i] <= 3 for i in range(len(r) - 1))
        decreasing = all(1 <= r[i] - r[i+1] <= 3 for i in range(len(r) - 1))
        return increasing or decreasing

    if is_increasing_or_decreasing(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_increasing_or_decreasing(modified_report):
            return True

    return False

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
