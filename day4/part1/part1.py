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

def find_xmas(grid):
    if not grid or not grid[0]:
        return 0, []
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    positions = [] 
    
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def check_direction(row, col, dx, dy):
        if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
            return False, []
        
        word = ''
        curr_positions = []
        for i in range(4):  
            curr_row = row + i*dx
            curr_col = col + i*dy
            word += grid[curr_row][curr_col]
            curr_positions.append((curr_row, curr_col))
            
        return word == 'XMAS', curr_positions
    
    found_positions = []
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                found, pos = check_direction(row, col, dx, dy)
                if found:
                    count += 1
                    found_positions.append(pos)
    
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
        count, positions = find_xmas(grid)
        
        print("\nOriginal grid:")
        for row in grid:
            print(row)
        
        print("\nHighlighted grid (only XMAS occurrences):")
        print_grid_with_highlights(grid, positions)
        
        print(f"\nTotal occurrences of XMAS: {count}")

if __name__ == "__main__":
    main()