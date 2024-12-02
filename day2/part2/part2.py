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

def can_be_safe_with_removal(numbers):
    if is_safe_sequence(numbers):
        return True
    
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i+1:]
        if is_safe_sequence(test_sequence):
            return True
    
    return False

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
    # input_file_path = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(__file__)
    input_file = os.path.join(current_dir, 'input.txt')
    
    reports = read_reports(input_file)
    if reports is not None:
        safe_count = 0
        for report in reports:
            if can_be_safe_with_removal(report):
                safe_count += 1
                # print(f"Safe sequence (possibly with removal): {report}")  
        
        print(f"Number of safe reports with Problem Dampener: {safe_count}")

if __name__ == "__main__":
    main()
