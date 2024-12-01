def read_input(file_path):
    left_list = []
    right_list = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into left and right numbers
                left, right = line.strip().split()
                left_list.append(int(left))
                right_list.append(int(right))
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None, None
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    
    # Convert right list to a list for counting occurrences
    right_numbers = right_list
    
    # Process each number in the left list
    for num in left_list:
        # Count how many times the current number appears in the right list
        occurrences = right_numbers.count(num)
        # Add to total score: number * occurrences
        total_score += num * occurrences
    
    return total_score

def main():
    # Use 'input.txt' from the same directory
    file_path = 'input.txt'
    
    # Read the input lists
    left_list, right_list = read_input(file_path)
    
    if left_list is None or right_list is None:
        return
    
    # Calculate and print the similarity score
    result = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score is: {result}")

if __name__ == "__main__":
    main()