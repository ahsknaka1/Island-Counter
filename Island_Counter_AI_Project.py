import matplotlib.pyplot as plt
import numpy as np
import random

def generate_dynamic_grid(rows, cols, land_density):
    """Generate a dynamic grid with random land and water."""
    return [[1 if random.random() < land_density else 0 for _ in range(cols)] for _ in range(rows)]

def visualize_grid(grid, title="Grid"):
    """Visualize the grid using matplotlib with visible boundaries."""
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="tab20", origin="upper")

    # Adding grid lines (boundaries)
    rows, cols = len(grid), len(grid[0])
    plt.xticks(np.arange(-0.5, cols, 1))
    plt.yticks(np.arange(-0.5, rows, 1))
    plt.grid(color='black', linestyle='-', linewidth=0.5)

    # Adjusting the grid to align with cell boundaries
    plt.gca().set_xticks(np.arange(-0.5, cols, 1), minor=True)
    plt.gca().set_yticks(np.arange(-0.5, rows, 1), minor=True)
    plt.gca().grid(which="minor", color="black", linestyle='-', linewidth=0.5)

    # Turn on the axis to see grid lines
    plt.gca().tick_params(axis='both', which='both', length=0)  # Hide tick marks
    plt.axis("on")  # Ensure the axis is visible

    # Adding colorbar and title
    plt.colorbar(label="Island ID")
    plt.title(title)
    plt.show()


def count_and_visualize_islands(grid):
    """Count islands and visualize them dynamically."""
    if not grid:
        print("Empty grid!")
        return 0, []

    rows, cols = len(grid), len(grid[0])
    island_id = 2  # Start marking islands with numbers > 1
    island_sizes = []

    def dfs(r, c, current_id):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = current_id  # Mark the cell with the current island ID
        size = 1  # Count the current cell
        # Explore all 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            size += dfs(r + dr, c + dc, current_id)
        return size

    # Visualize the original grid
    visualize_grid(np.array(grid), title="Original Grid")

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Found an unvisited island cell
                size = dfs(r, c, island_id)
                island_sizes.append(size)
                island_id += 1

    # Visualize the grid with islands marked
    visualize_grid(np.array(grid), title="Islands Identified")

    return island_id - 2, island_sizes  # Return the number of islands and their sizes

# User-defined grid dimensions and land density
rows = int(input("Enter the number of rows for the grid: "))
cols = int(input("Enter the number of columns for the grid: "))
land_density = float(input("Enter the land density (0.0 to 1.0): "))

# Generate dynamic grid
dynamic_grid = generate_dynamic_grid(rows, cols, land_density)

# Count and visualize islands
island_count, island_sizes = count_and_visualize_islands(dynamic_grid)
print("Number of islands:", island_count)
print("Sizes of islands:", island_sizes)