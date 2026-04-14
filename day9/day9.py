def part1(input_arr):
    val = 0
    
    for i in range(len(input_arr)):
        for j in range(i+1, len(input_arr)):
            val = max((abs(input_arr[i][0]-input_arr[j][0])+1)*(abs(input_arr[i][1]-input_arr[j][1])+1), val)
    print("Day 9 Part 1:", val)

def part2(input_arr):
    val = 0
    print("Day 9 Part 2:", val)

if __name__ == '__main__':        
    input_arr = []
    inputfile = 'day9/day9test.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            input_arr.append([int(x) for x in i.strip().split(',')])
        f.close()


    part1(input_arr)
    part2(input_arr)

