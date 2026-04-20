def part1(data):

    for target, data in data.items():
        print(target, data['button_combos'])

    result = None
    print(f"Day 10 Part 1: {result}")


def part2(data):
    """Part 2 solution"""
    result = None
    print(f"Day 10 Part 2: {result}")


if __name__ == '__main__':
    # Read input from file
    inputfile = 'day10/day10test.txt'
    data = {}
    with open(inputfile, 'r') as f:
        for line in f:
            line = line.strip().split()
            target_lights = line[0][1:len(line[0])-1]
            data[target_lights] = {}
            data[target_lights]['button_combos'] = [(v,) if isinstance(v, int) else v for x in line[1:-1] for v in (eval(x),)]
            data[target_lights]['button_joltages'] = list(eval(line[len(line)-1]))
    part1(data)
    part2(data)
