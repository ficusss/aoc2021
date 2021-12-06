import sys
from collections import deque


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        measurements = [int(line) for line in fp.readlines() if line.strip()]

    # part1
    count_dives = find_count_dives_by_window(measurements)
    print('Count dives (window=1) is %s' % count_dives)

    # part2
    count_dives = find_count_dives_by_window(measurements, window=3)
    print('Count dives (window=3) is %s' % count_dives)


def find_count_dives_by_window(measurements: list[int], window: int = 1) -> int:
    count_dives = 0

    measurements_in_window = deque(measurements[:window], maxlen=window)
    for measurement in measurements[window:]:
        prev_measurement =  sum(measurements_in_window)
        measurements_in_window.append(measurement)
        curr_measurement = sum(measurements_in_window)
        count_dives += int(curr_measurement > prev_measurement)

    return count_dives


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
