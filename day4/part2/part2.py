import os

def read_grid(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def is_mas(s):
    return s in ['MAS', 'SAM']

def find_x_mas(grid):
    if not grid or not grid[0]:
        return 0, []
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    found_positions = []
    
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            diagonal1 = grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]  # Top-left to bottom-right
            diagonal2 = grid[row-1][col+1] + grid[row][col] + grid[row+1][col-1]  # Top-right to bottom-left
            
            diagonal1_rev = diagonal1[::-1]  
            diagonal2_rev = diagonal2[::-1]  
            
            if ((is_mas(diagonal1) or is_mas(diagonal1_rev)) and 
                (is_mas(diagonal2) or is_mas(diagonal2_rev))):
                count += 1
                x_positions = [
                    (row-1, col-1), 
                    (row-1, col+1), 
                    (row, col),     
                    (row+1, col-1), 
                    (row+1, col+1)  
                ]
                found_positions.append(x_positions)
    
    return count, found_positions

def print_grid_with_highlights(grid, positions):
    highlighted_grid = [[char for char in row] for row in grid]
    
    flat_positions = {pos for sequence in positions for pos in sequence}
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in flat_positions:
                highlighted_grid[i][j] = '.'
    
    for row in highlighted_grid:
        print(''.join(row))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    
    grid = read_grid(input_path)
    
    if grid:
        count, positions = find_x_mas(grid)
        
        print("\nOriginal grid:")
        for row in grid:
            print(row)
        
        print("\nHighlighted grid (only X-MAS occurrences):")
        print_grid_with_highlights(grid, positions)
        
        print(f"\nTotal occurrences of X-MAS: {count}")

if __name__ == "__main__":
    main()