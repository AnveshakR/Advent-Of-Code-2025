import math

def calculate_and_sort_pairs(junction_box_coords):
    pairs = []
    for i in range(len(junction_box_coords)):
        for j in range(i+1, len(junction_box_coords)):
            dist = round(math.sqrt(sum([(junction_box_coords[i][x]-junction_box_coords[j][x])**2 for x in range(3)])))
            pairs.append((dist, i, j))
    return sorted(pairs, key=lambda x: x[0])

def build_circuits(parent, num_circuits):
    circuits = {}
    for i in range(num_circuits):
        root = find_root(parent, i)
        if root not in circuits:
            circuits[root] = set()
        circuits[root].add(i)
    return circuits

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find_root(parent, x)
    root_y = find_root(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def part1(junction_box_coords, pairs):
    val = 1
    parent = list(range(len(junction_box_coords)))

    for _, i, j in pairs[:len(junction_box_coords)]:
        union(parent, i, j)

    circuits = build_circuits(parent, len(junction_box_coords))
    lengths = sorted([len(c) for c in circuits.values()], reverse=True)[:3]
    for length in lengths:
        val *= length

    print("Day 8 Part 1:", val)

def part2(junction_box_coords, pairs):
    import time
    start = time.time()
    val = 1
    parent = list(range(len(junction_box_coords)))

    for _, i, j in pairs:
        union(parent, i, j)

        if len(set(find_root(parent, k) for k in range(len(junction_box_coords)))) == 1:
            val = junction_box_coords[i][0] * junction_box_coords[j][0]
            break

    print("Day 8 Part 2:", val)

if __name__ == '__main__':
    junction_box_coords = []
    inputfile = 'day8/day8input.txt'
    with open(inputfile, 'r') as f:
        for i in f.readlines():
            junction_box_coords.append(list(map(int, i.strip().split(','))))
        f.close()

    pairs = calculate_and_sort_pairs(junction_box_coords)

    part1(junction_box_coords, pairs)
    part2(junction_box_coords, pairs)

