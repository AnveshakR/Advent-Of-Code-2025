def part1(number_rows, operands):
    val = 0

    for i in range(len(operands)):
        if operands[i] == '+':
            temp = 0
            for j in range(len(number_rows)):
                temp+=int(number_rows[j][i])
        else:
            temp = 1
            for j in range(len(number_rows)):
                temp*=int(number_rows[j][i])
    
        val+=temp
    print("Day 6 Part 1:", val)

def part2(number_rows, operands):
    from functools import reduce
    val = 0
    final_numbers = []
    number_rows = [' ' + row for row in number_rows]
    operands = ' ' + operands

    for i in range(len(number_rows[0])-1, -1, -1):
        curr = ''.join(row[i] for row in number_rows)
        if curr == ' ' * len(number_rows):
            if operands[i+1] == '+':
                val += sum(final_numbers)
            elif operands[i+1] == '*':
                val += reduce(lambda x, y: x * y, final_numbers)
            final_numbers = []
        else:
            final_numbers.append(int(curr))

    print("Day 6 Part 2:", val)

if __name__ == '__main__':        
    input_arr = []
    input_str = []

    inputfile = 'day6/day6test.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            input_arr.append(i.strip().split())
        f.close()
    
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            input_str.append(i[:-1])
        f.close()

    part1(input_arr[:-1], input_arr[-1])
    part2(input_str[:-1], input_str[-1])

