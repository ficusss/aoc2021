import sys
import random
from typing import Callable, TypeVar


TNum = TypeVar('TNum', int, float)


def main():
    crabs_positions  = parse_input_data(sys.argv[1])
    # print("Crabs positions: ", crabs_positions)

    #part1
    if len(crabs_positions) % 2 == 1:
        optimal_crabs_position = quickselect(crabs_positions, len(crabs_positions) // 2, select_pivot)
    else:
        optimal_crabs_position = quickselect(crabs_positions, len(crabs_positions) // 2 - 1, select_pivot)
    fuel_need = sum([abs(crab_pos - optimal_crabs_position) for crab_pos in crabs_positions])
    print("The cheapest possible outcome in position {} with а cost {} fuel.".format(optimal_crabs_position, fuel_need))

    #part2
    fuel_need_for_position = []
    for position in range(min(crabs_positions), max(crabs_positions)):
        fnfp = sum([sum(range(abs(crab_pos - position) + 1)) for crab_pos in crabs_positions])
        fuel_need_for_position.append(fnfp)

        # for crab_pos in crabs_positions:
        #     print(f"Move from {crab_pos} to {position}: {sum(range(abs(crab_pos - position) + 1))}")
        # print(fnfp)

    fuel_need = min(fuel_need_for_position)
    optimal_crabs_position = fuel_need_for_position.index(fuel_need) + min(crabs_positions)
    print("Crab Engineering: The cheapest possible outcome in position {} with а cost {} fuel.".format(optimal_crabs_position, fuel_need))



def parse_input_data(filepath: str) -> list[int]:
    with open(filepath, 'r') as fp:
        crabs = [int(n) for n in fp.readline().split(',')]
    return crabs


def quickselect(collection: list[TNum], position: int, pivot_fn: Callable) -> TNum:
    while True:
        if len(collection) == 1:
            assert position == 0
            return collection[0]
        
        pivot = pivot_fn(collection)

        lows = []
        hights = []
        pivots = []
        for element in collection:
            if element < pivot:
                lows.append(element)
            elif element > pivot:
                hights.append(element)
            else:
                pivots.append(element)

        if len(lows) > position:
            collection = lows
        elif position > len(lows) + len(pivots):
            collection =  hights
            position -= len(lows) + len(pivots)
        else:
            return pivots[0]


def select_pivot(collection: list[TNum]) -> TNum:
    return random.choice(collection)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
