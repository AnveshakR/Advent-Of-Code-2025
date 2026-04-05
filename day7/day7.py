def part1(data):
    result = 0
    curr_beams = set([data[0].find("S")])
    for row in data[1:]:
        if row.find("^") == -1:
            continue
        splitter_indices = [i for i, c in enumerate(row) if c == "^"]
        for i in splitter_indices:
            if i in curr_beams:
                curr_beams.remove(i)
                curr_beams.update([i + 1, i - 1])
                result += 1

    print(f"Day 7 Part 1: {result}")


def part2(data):
    rows = len(data)
    start_col = data[0].find("S")
    
    def get_next_positions(row, col):
        r = row
        while r + 1 < rows and data[r + 1][col] == '.':
            r += 1
        
        if r + 1 >= rows:
            return []
        
        return [(r + 2, col - 1), (r + 2, col + 1)]
    memo = {}
    
    def count_paths(row, col):
        key = (row, col)
        if key in memo:
            return memo[key]
        
        next_positions = get_next_positions(row, col)
        if not next_positions:
            memo[key] = 1 
            return 1

        total = sum(count_paths(nr, nc) for nr, nc in next_positions)
        memo[key] = total
        return total
    
    result = count_paths(0, start_col)
    print(f"Day 7 Part 2: {result}")


if __name__ == "__main__":
    # Read input from file
    inputfile = "day7/day7input.txt"
    data = []
    with open(inputfile, "r") as f:
        for line in f:
            data.append(line.strip())

    # print(data)
    part1(data)
    part2(data)