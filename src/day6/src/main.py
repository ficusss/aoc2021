import sys
from collections import deque


point_type = tuple[int, int]
vector_type = tuple[point_type, point_type]


def main():
    main_loop, first_loop  = parse_input_data(sys.argv[1])

    count_days = 256
    main_loop, first_loop = simulation_population(main_loop, first_loop, count_days)
    total_population_count = sum(main_loop) + sum(first_loop)
    print(f"Total population after {count_days} days is {total_population_count}")


def parse_input_data(filepath: str) -> tuple[deque, deque]:

    with open(filepath, 'r') as fp:
        data = [int(n) for n in fp.readline().split(',')]
        first_loop = deque([data.count(8), data.count(7)], maxlen=2)
        main_loop = deque(
            [
                data.count(6),
                data.count(5), 
                data.count(4), 
                data.count(3), 
                data.count(2),
                data.count(1), 
                data.count(0)
            ],
            maxlen=7
        )

    return main_loop, first_loop


def simulation_population(main_loop: deque, first_loop: deque, count_days: int) -> tuple[deque, deque]:
    for _ in range(count_days):
        count_birth = main_loop.pop()
        count_first_to_main = first_loop.pop()
        first_loop.appendleft(count_birth)
        main_loop.appendleft(count_birth + count_first_to_main)

    return main_loop, first_loop
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
