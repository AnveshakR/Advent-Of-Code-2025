def part1(input_arr):
    val = 0

    for i in range(len(input_arr)):
        for j in range(i + 1, len(input_arr)):
            val = max(
                (abs(input_arr[i][0] - input_arr[j][0]) + 1)
                * (abs(input_arr[i][1] - input_arr[j][1]) + 1),
                val,
            )
    print("Day 9 Part 1:", val)


def part2(input_arr):
    points = [tuple(p) for p in input_arr]
    red_set = set(points)
    polygon = points + [points[0]]

    def get_other_corners(corner1, corner2):
        return (corner1[0], corner2[1]), (corner2[0], corner1[1])

    def get_area(corner1, corner2):
        return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

    def rectangle_edges_clear(c1, c2):
        xmin, xmax = (c1[0], c2[0]) if c1[0] < c2[0] else (c2[0], c1[0])
        ymin, ymax = (c1[1], c2[1]) if c1[1] < c2[1] else (c2[1], c1[1])
        for v in range(len(polygon) - 1):
            (x1, y1), (x2, y2) = polygon[v], polygon[v + 1]
            if y1 == y2:
                a, b = (x1, x2) if x1 < x2 else (x2, x1)
                if ymin < y1 < ymax and a < xmax and b > xmin:
                    return False
            else:
                a, b = (y1, y2) if y1 < y2 else (y2, y1)
                if xmin < x1 < xmax and a < ymax and b > ymin:
                    return False
        return True

    def ray_crosses_edge(point, seg1, seg2):
        px, py = point
        x1, y1 = seg1
        x2, y2 = seg2
        if (y1 <= py < y2) or (y2 <= py < y1):
            if px < (x2 - x1) * (py - y1) / (y2 - y1) + x1:
                return 1
        return 0

    def is_on_boundary(point):
        px, py = point
        for i in range(len(polygon) - 1):
            x1, y1 = polygon[i]
            x2, y2 = polygon[i + 1]
            if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
                cross = (py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)
                if cross == 0:
                    return True
        return False

    def corner_inside(corner):
        if corner in red_set or is_on_boundary(corner):
            return True
        count = 0
        for v in range(len(polygon) - 1):
            count += ray_crosses_edge(corner, polygon[v], polygon[v + 1])
        return count % 2 == 1

    n = len(points)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    pairs.sort(key=lambda p: get_area(points[p[0]], points[p[1]]), reverse=True)

    val = 0
    for i, j in pairs:
        p1, p2 = points[i], points[j]
        corner3, corner4 = get_other_corners(p1, p2)
        if (
            corner_inside(corner3)
            and corner_inside(corner4)
            and rectangle_edges_clear(p1, p2)
        ):
            val = get_area(p1, p2)
            break

    print("Day 9 Part 2:", val)


if __name__ == "__main__":
    input_arr = []
    inputfile = "day9/day9input.txt"
    with open(inputfile, "r") as f:
        for i in f.readlines():
            input_arr.append([int(x) for x in i.strip().split(",")])
        f.close()

    part1(input_arr)
    part2(input_arr)
