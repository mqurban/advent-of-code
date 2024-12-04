import os
import re

def extract_multiplications(text):
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    
    matches = re.finditer(pattern, text)
    
    total = 0
    multiplications = []
    
    # Process each match
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 * num2
        total += result
        multiplications.append((num1, num2, result))
        
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
        
        print(f"\nFound multiplications:")
        for num1, num2, result in multiplications:
            print(f"mul({num1},{num2}) = {result}")
        
        print(f"\nTotal sum of all multiplications: {total}")

if __name__ == "__main__":
    main()