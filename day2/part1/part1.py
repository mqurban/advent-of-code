import os

def is_safe_sequence(numbers):
    if len(numbers) < 2:
        return False
        
    increasing = numbers[1] > numbers[0]
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        if increasing and diff <= 0:
            return False
            
        if not increasing and diff >= 0:
            return False
    
    return True

def read_reports(filename):
    reports = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers = list(map(int, line.strip().split()))
                reports.append(numbers)
        return reports
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError:
        print("Error: File should contain space-separated numbers.")
        return None

def main():
    current_dir = os.path.dirname(__file__)
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')
    
    reports = read_reports(input_path)
    if reports is not None:
        safe_count = 0
        for report in reports:
            if is_safe_sequence(report):
                safe_count += 1
                # print(f"Safe sequence: {report}")  
        
        print(f"Number of safe reports: {safe_count}")

if __name__ == "__main__":
    main()
