def part1(fresh_ranges, available_ingredients):
    val = 0
    for ingredient in available_ingredients:
        for ranges in fresh_ranges:
            if ingredient >= ranges[0] and ingredient <= ranges[1]:
                val+=1
                break
                
    print("Day 5 Part 1:", val)

def part2(fresh_ranges):
    val = 0
    final_ranges = []
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    flag = 0
    for i in range(len(sorted_ranges)-1):
        i = flag
        curr = sorted_ranges[i]
        for j in range(i+1, len(sorted_ranges)):
            if curr[1] >= sorted_ranges[j][1]:
                continue
            if curr[1] >= sorted_ranges[j][0]:
                curr[1] = sorted_ranges[j][1]
            else:
                flag = j
                break
        final_ranges.append(curr)
        if flag == i:
            break
        
    for i in final_ranges:
        val += i[1] - i[0] + 1
    print("Day 5 Part 2:", val)

if __name__ == '__main__':        
    fresh_ranges = []
    available_ingredients = []
    inputfile = 'day5/day5input.txt'
    with open(inputfile, 'r') as f:
        i = f.read().split("\n\n")
        for j in i[0].split("\n"):
            fresh_ranges.append([int(x) for x in j.strip().split('-')])
        for j in i[1].split("\n"):
            available_ingredients.append(int(j))

        f.close()

    part1(fresh_ranges, available_ingredients)
    part2(fresh_ranges)

