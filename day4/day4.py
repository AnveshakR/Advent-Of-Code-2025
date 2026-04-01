import copy
nn_operators = [
    [-1, 0], # W,
    [1, 0], # E
    [0, -1], # N
    [0, 1], # S
    [-1, -1], #NW
    [-1, 1], #SW
    [1, -1], #NE
    [1, 1], #NW
    ]
def part1(input_grid, called=False):
    final_grid = copy.deepcopy(input_grid)
    val = 0
    rows, cols = len(input_grid), len(input_grid[0])
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != '@':
                continue
            count = 0
            for op in nn_operators:
                ni, nj = i + op[0], j + op[1]
                if 0 <= ni < rows and 0 <= nj < cols:
                    if input_grid[ni][nj] == '@':
                        count += 1
            if count < 4:
                final_grid[i] = final_grid[i][0:j] + '.' + final_grid[i][j+1:]
                val += 1
    if not called:
        print("Day 4 Part 1:", val)
    return final_grid, val

def part2(input_grid):
    val = 0
    last_grid = input_grid
    while(True):
        final_grid, removed_rolls = part1(last_grid, True)
        val+=removed_rolls
        if final_grid == last_grid:
            break
        last_grid = final_grid

    print("Day 4 Part 2:", val)

if __name__ == '__main__':        
    input_grid = []
    inputfile = 'day4/day4input.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            input_grid.append(i.strip())
        f.close()

    part1(input_grid)
    part2(input_grid)

