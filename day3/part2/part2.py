import os
import re

def extract_multiplications(text):
    control_pattern = r'(?:do|don\'t)\(\)'
    mul_pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    
    operations = []
    current_pos = 0
    
    combined_pattern = f'({control_pattern}|{mul_pattern})'
    matches = re.finditer(combined_pattern, text)
    
    total = 0
    multiplications = []
    enabled = True  
    
    for match in matches:
        operation = match.group(0)
        
        if operation == 'do()':
            enabled = True
        elif operation == "don't()":
            enabled = False
        else:
            if enabled:  
                num1 = int(match.group(2)) 
                num2 = int(match.group(3))
                result = num1 * num2
                total += result
                multiplications.append((num1, num2, result, True))
            else:
                num1 = int(match.group(2))
                num2 = int(match.group(3))
                multiplications.append((num1, num2, num1 * num2, False))
    
    return total, multiplications

def read_input(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    
    corrupted_memory = read_input(input_path)
    
    if corrupted_memory:
        total, multiplications = extract_multiplications(corrupted_memory)
        
        print("\nFound multiplications:")
        for num1, num2, result, enabled in multiplications:
            status = "ENABLED" if enabled else "DISABLED"
            print(f"mul({num1},{num2}) = {result} [{status}]")
        
        print(f"\nTotal sum of enabled multiplications: {total}")

if __name__ == "__main__":
    main()