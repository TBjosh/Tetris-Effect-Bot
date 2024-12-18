def score_grid(grid):
    """
    Calculate a score for the grid:
    - Clear lines = +points
    - Holes = -points
    - Flat surface = +points
    """
    lines_cleared = sum(1 for row in grid if all(row))
    holes = sum(
        1 for x in range(len(grid[0]))
        for y in range(1, len(grid))
        if grid[y][x] == 0 and grid[y - 1][x] == 1
    )
    flatness = -np.std([sum(row) for row in zip(*grid)])  # Reward flat surfaces

    return (lines_cleared * 10) - (holes * 5) + flatness
