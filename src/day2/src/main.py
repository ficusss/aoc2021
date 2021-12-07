import sys
from typing import Tuple


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        planned_course = []
        for line in fp.readlines():
            if not line.strip():
                continue
            course, value = line.strip().split()
            value = int(value)
            planned_course.append((course, value))

    # part1
    horizontal, depth = find_coordinates(planned_course)
    print('A horizontal position of %s and a depth of %s.(Multiplying = %s)' % (horizontal, depth, horizontal * depth))

    # part2
    horizontal, depth = find_coordinates_with_aim(planned_course)
    print('AIM: A horizontal position of %s and a depth of %s.(Multiplying = %s)' % (horizontal, depth, horizontal * depth))


def find_coordinates(planned_course: list[tuple[str, int]]) -> tuple[int, int]:
    horizontal, depth = 0, 0

    for course, value in planned_course:
        if course == 'forward':
            horizontal += value
        elif course == 'down':
            depth += value
        elif course == 'up':
            depth -= value

    return horizontal, depth


def find_coordinates_with_aim(planned_course: list[tuple[str, int]]) -> tuple[int, int]:
    horizontal, depth, aim = 0, 0, 0

    for course, value in planned_course:
        if course == 'forward':
            horizontal += value
            depth += aim * value
        elif course == 'down':
            aim += value
        elif course == 'up':
            aim -= value

    return horizontal, depth


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
