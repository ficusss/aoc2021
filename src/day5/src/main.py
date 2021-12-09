import sys
import numpy as np


point_type = tuple[int, int]
vector_type = tuple[point_type, point_type]


def main():
    vectors, x_max, y_max  = parse_input_data(sys.argv[1])

    # part1
    map = create_horizontal_vertical_map(vectors, x_max, y_max)
    print(map)
    print((map >= 2).sum())

    # part2
    map = create_full_map(vectors, x_max, y_max)
    print(map)
    print((map >= 2).sum())


def parse_input_data(filepath: str) -> tuple[list[vector_type], int, int]:

    with open(filepath, 'r') as fp:
        vectors = []
        x_max, y_max = 0, 0
        for line in fp.readlines():
            (x1, y1), (x2, y2) = (p.strip().split(',') for p in line.split('->'))
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            vectors.append(((x1, y1), (x2, y2)))
            x_max, y_max = int(np.max([x_max, x1, x2])), int(np.max([y_max, y1, y2]))

    return vectors, x_max, y_max


def create_horizontal_vertical_map(vectors: list[vector_type], x_max: int, y_max: int) -> np.ndarray:
    map = np.zeros((y_max+1, x_max+1))
    
    for p1, p2 in vectors:
        if p1[0] != p2[0] and p1[1] != p2[1]:
            continue

        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        if x_min != x_max:
            for icol in range(x_min, x_max+1):
                map[p1[1], icol] += 1

        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        if y_min != y_max:
            for irow in range(y_min, y_max+1):
                map[irow, p1[0]] += 1
    
    return map


def create_full_map(vectors: list[vector_type], x_max: int, y_max: int) -> np.ndarray:
    map = np.zeros((y_max+1, x_max+1))
    
    for p1, p2 in vectors:
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

        if p1[0] != p2[0] and p1[1] != p2[1]:
            p1, p2 = complex(*p1), complex(*p2)
            p_diff = p2 - p1
            x1, x2, x_step = int(p1.real), int(p2.real), int(np.sign(p_diff.real))
            y1, y2, y_step = int(p1.imag), int(p2.imag), int(np.sign(p_diff.imag))
            points = list(zip(range(x1, x2+x_step, x_step), range(y1, y2+y_step, y_step)))
            for icol, irow in points:
                map[irow, icol] += 1
            continue

        if x_min != x_max:
            for icol in range(x_min, x_max+1):
                map[p1[1], icol] += 1

        if y_min != y_max:
            for irow in range(y_min, y_max+1):
                map[irow, p1[0]] += 1
    
    return map
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
