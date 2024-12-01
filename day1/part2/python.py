def read_input(file_path):
    left_list = []
    right_list = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                left, right = line.strip().split()
                left_list.append(int(left))
                right_list.append(int(right))
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None, None
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    
    right_numbers = right_list
    
    for num in left_list:
        occurrences = right_numbers.count(num)
        total_score += num * occurrences
    
    return total_score

def main():
    file_path = 'input.txt'
    left_list, right_list = read_input(file_path)
    if left_list is None or right_list is None:
        return
    result = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score is: {result}")

if __name__ == "__main__":
    main()