import numpy as np

# Define the game grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Define Tetrimino shapes (using 2D arrays)
TETRIMINOS = {
    'I': np.array([[1, 1, 1, 1]]),
    'O': np.array([[1, 1], [1, 1]]),
    'T': np.array([[0, 1, 0], [1, 1, 1]]),
    'L': np.array([[1, 0], [1, 0], [1, 1]]),
    'J': np.array([[0, 1], [0, 1], [1, 1]]),
    'S': np.array([[0, 1, 1], [1, 1, 0]]),
    'Z': np.array([[1, 1, 0], [0, 1, 1]]),
}

# Initialize an empty game grid
def create_empty_grid():
    return np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

# Print the game grid for visualization
def print_grid(grid):
    for row in grid:
        print("".join(["■" if cell else " " for cell in row]))
    print("-" * GRID_WIDTH)

# Check for collisions
def is_collision(grid, piece, x, y):
    shape = TETRIMINOS[piece]
    for row_idx, row in enumerate(shape):
        for col_idx, val in enumerate(row):
            # Check out-of-bounds conditions
            grid_x = x + col_idx
            grid_y = y + row_idx
            if val == 1:
                if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y < 0 or grid_y >= GRID_HEIGHT:
                    return True  # Out of bounds
                if grid[grid_y, grid_x] == 1:
                    return True  # Overlaps with an existing block
    return False

# Place a Tetrimino on the grid if no collision
def place_tetrimino(grid, piece, x, y):
    if is_collision(grid, piece, x, y):
        print(f"Collision detected! Cannot place '{piece}' at ({x}, {y})")
        return grid  # Return grid unchanged
    shape = TETRIMINOS[piece]
    for row_idx, row in enumerate(shape):
        for col_idx, val in enumerate(row):
            if val == 1:  # Place the block if it's part of the piece
                grid[y + row_idx, x + col_idx] = 1
    return grid

# Test placing pieces on the grid with collision detection
def main():
    grid = create_empty_grid()
    print("Initial Grid:")
    print_grid(grid)

    # Place a 'T' piece at (3, 0)
    print("Placing a 'T' piece at (3, 0):")
    grid = place_tetrimino(grid, 'T', 3, 0)
    print_grid(grid)

    # Attempt to place a 'T' piece at (8, 0) (near the right edge)
    print("Placing a 'T' piece at (8, 0):")
    grid = place_tetrimino(grid, 'T', 8, 0)
    print_grid(grid)

    # Attempt to place a 'L' piece overlapping the existing 'T'
    print("Placing an 'L' piece at (3, 1):")
    grid = place_tetrimino(grid, 'L', 3, 1)
    print_grid(grid)

    # Attempt to place a 'Z' piece out of bounds
    print("Placing a 'Z' piece at (9, 19):")
    grid = place_tetrimino(grid, 'Z', 9, 19)
    print_grid(grid)

if __name__ == "__main__":
    main()