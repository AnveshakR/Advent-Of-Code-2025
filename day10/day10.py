import numpy as np
from itertools import combinations


def part1(data):
    result = 0
    for entry in data:
        target = entry["target"]
        button_data = entry

        results_dict = {}
        for r in range(0, len(button_data["button_combos"]) + 1):
            for combo in combinations(range(len(button_data["button_combos"])), r):
                row_sum = tuple(
                    button_data["button_combos"][list(combo)].sum(axis=0) % 2
                )
                row_sum = tuple(int(x) for x in row_sum)
                results_dict.setdefault(row_sum, []).append(combo)

        target_tuple = tuple(int(c == "#") for c in target)
        min_combo = min(results_dict[target_tuple], key=len)
        shortest_combo = len(min_combo)

        result += shortest_combo

    print(f"Day 10 Part 1: {result}")


def part2(data):
    """Part 2 solution"""
    result = None
    print(f"Day 10 Part 2: {result}")


if __name__ == "__main__":

    inputfile = "day10/day10input.txt"
    data = []
    with open(inputfile, "r") as f:
        for line in f:
            line = line.strip().split()
            target_lights = line[0][1 : len(line[0]) - 1]
            entry = {}
            entry["target"] = target_lights
            entry["button_combos"] = np.array(
                [
                    [1 if i in combo else 0 for i in range(len(target_lights))]
                    for combo in [
                        (v,) if isinstance(v, int) else v
                        for x in line[1:-1]
                        for v in (eval(x),)
                    ]
                ],
                dtype=int,
            )
            entry["button_joltages"] = list(eval(line[len(line) - 1]))
            data.append(entry)
    part1(data)
    part2(data)
