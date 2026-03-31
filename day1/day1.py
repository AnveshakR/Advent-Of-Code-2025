start = 50

def part1(input_combinations):
    pos = start
    count = 0
    for i in input_combinations:
        if i[0] == 'R':
            pos += i[1]
        elif i[0] == 'L':
            pos -= i[1]
        pos %= 100
        if pos == 0:
            count += 1
    print("Day 1 Part 1:", count)

def part2(input_combinations):
    pos = start
    count = 0
    for i in input_combinations:
        if i[0] == 'R':
            new_pos = pos + i[1]
            count += new_pos // 100 - pos // 100
        else:
            new_pos = pos - i[1]
            count += (pos - 1) // 100 - (new_pos - 1) // 100
        pos = new_pos % 100
    print("Day 1 Part 2:", count)

if __name__ == '__main__':        
    input_combinations = []
    inputfile = 'day1/day1test.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            input_combinations.append((i.strip()[0], int(i.strip()[1:])))
        f.close()

    # print(input_combinations)

    part1(input_combinations)
    part2(input_combinations)

