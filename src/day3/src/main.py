import sys
from typing import Tuple


def main():
    input_filepath = sys.argv[1]
    with open(input_filepath, 'r') as fp:
        numbers = [line.strip() for line in fp.readlines() if line.strip()]

    # part1
    gamma_rate, epsilon_rate = find_gamma_and_epsilon_rate(numbers)
    print('A gamma rate of %s and a epsilon rate of %s.(Multiplying = %s)' % (gamma_rate, epsilon_rate, gamma_rate * epsilon_rate))

    # part2
    oxygen_rating = find_oxygen_rating(numbers)
    scrubber_rating = find_scrubber_rating(numbers)
    print('A oxygen rating of %s and a scrubber rating of %s.(Multiplying = %s)' % (oxygen_rating, scrubber_rating, oxygen_rating * scrubber_rating))


def find_gamma_and_epsilon_rate(numbers: list[str]) -> tuple[int, int]:
    half_count_numbers = len(numbers) // 2

    splited_numbers = [list(map(int, n)) for n in numbers]
    binary_gamma_rate = []
    binary_epsilon_rate = []
    for numbers_of_rank  in zip(*splited_numbers):
        count = sum(numbers_of_rank)
        binary_gamma_rate.append(str(int(count > half_count_numbers)))
        binary_epsilon_rate.append(str(int(count < half_count_numbers)))

    gamma_rate = int(''.join(binary_gamma_rate), 2)
    epsilon_rate = int(''.join(binary_epsilon_rate), 2)

    return gamma_rate, epsilon_rate


def find_oxygen_rating(numbers: list[str]) -> int:
    oxygen_numbers = numbers
    oxygen_rating = -1

    for count_try in range(len(numbers[0])):
        for rank in range(count_try, len(numbers[0])):
            half_count_numbers = len(oxygen_numbers) / 2
            splited_oxygen_numbers = [list(map(int, n)) for n in oxygen_numbers]
            ranks_value = list(zip(*splited_oxygen_numbers))
            count_one = int(sum(ranks_value[rank]))
            most_common_value = '1' if count_one >= half_count_numbers else '0'
            
            oxygen_numbers = [
                oxygen_number for oxygen_number in oxygen_numbers 
                if oxygen_number[rank] == most_common_value
            ]
            
            if len(oxygen_numbers) == 1:
                oxygen_rating = int(oxygen_numbers[0], 2)
                break
            
        if len(oxygen_numbers) == 1:
            break

    return oxygen_rating


def find_scrubber_rating(numbers: list[str]) -> int:
    scrubber_numbers = numbers
    scrubber_rating = -1

    for count_try in range(len(numbers[0])):
        for rank in range(count_try, len(numbers[0])):
            half_count_numbers = len(scrubber_numbers) / 2
            splited_scrubber_numbers = [list(map(int, n)) for n in scrubber_numbers]
            ranks_value = list(zip(*splited_scrubber_numbers))
            count_one = int(sum(ranks_value[rank]))
            most_common_value = '1' if count_one < half_count_numbers else '0'

            scrubber_numbers = [
                scrubber_number for scrubber_number in scrubber_numbers 
                if scrubber_number[rank] == most_common_value
            ]
            
            if len(scrubber_numbers) == 1:
                scrubber_rating = int(scrubber_numbers[0], 2)
                break

        if len(scrubber_numbers) == 1:
            break

    return scrubber_rating


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
