import re

def part1(ranges):
    invalid_id_sum = 0
    for i in ranges:
        for j in range(int(i[0]), int(i[1])+1):
            res = re.fullmatch(r"(.+)\1", str(j))
            if bool(res):
                invalid_id_sum+=j
    print("Day 2 Part 1:", invalid_id_sum)
    
def part2(ranges):
    invalid_id_sum = 0
    for i in ranges:
        for j in range(int(i[0]), int(i[1])+1):
            res = re.fullmatch(r"(.+)\1+", str(j))
            if bool(res):
                invalid_id_sum+=j

    print("Day 2 Part 2:", invalid_id_sum)

if __name__ == "__main__":
    inputfile = 'day2/day2input.txt'
    with open(inputfile, 'r') as f:
        ranges = f.readline().strip().split(',')
        f.close()
    for i in range(len(ranges)):
        ranges[i] = ranges[i].strip().split('-') # type: ignore

    part1(ranges)
    part2(ranges)