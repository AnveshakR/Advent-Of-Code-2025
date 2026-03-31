def part1(banks):
    val = 0
    for bank in banks:
        digit1 = int(bank[0])
        digit1pos = 0
        for i in range(1, len(bank)-1):
            if int(bank[i]) > digit1:
                digit1 = int(bank[i])
                digit1pos = i
        val+=(10*digit1)
        digit2 = 0
        for i in range(digit1pos+1, len(bank)):
            if int(bank[i]) > digit2:
                digit2 = int(bank[i])

        val+=digit2
        
    print("Day 1 Part 1:", val)

def part2(banks):
    
    print("Day 1 Part 2:")

if __name__ == '__main__':        
    banks = []
    inputfile = 'day3/day3input.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            banks.append(i.strip())
        f.close()


    part1(banks)
    part2(banks)

