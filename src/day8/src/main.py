from os import truncate
import sys


TInputLine = tuple[tuple[str, str, str, str, str, str, str, str, str, str], tuple[str, str, str, str]]


def main():
    encryptions  = parse_input_data(sys.argv[1])

    # part1
    decode_group = [s for encryption in encryptions for s in encryption[1] if len(s) in [2,3,4,7]]
    print(
        f"Counting only digits in the output values, there are {len(decode_group)} " \
        "instances of digits that use a unique number of segments."
    )

    # part2
    sum_encriprion_numbers = sum([int(decode_encryption(encryption)) for encryption in encryptions])
    print("Sum all of the output values is", sum_encriprion_numbers)


def parse_input_data(filepath: str) -> list[TInputLine]:
    result = []
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            unique_signal_patterns, output_values = (elem.strip() for elem in line.split("|"))
            unique_signal_patterns, output_values = tuple(unique_signal_patterns.split()), tuple(output_values.split())
            result.append((unique_signal_patterns, output_values))

    return result


def decode_encryption(encryption: TInputLine) -> str:

    encryption_keys, encryption_test = encryption
    encryption_keys = tuple(frozenset(key) for key in sorted(encryption_keys, key=len))
    one, seven, four, two, three, five, zero, six, nine, eight = encryption_keys

    for key in [two, three, five]:
        if key.issuperset(one):
            three = key
        elif key.issuperset(four - one):
            five = key
        else:
            two = key
    for key in [zero, six, nine]:
        if key.issuperset(four):
            nine = key
        elif key.issuperset(four - one):
            six = key
        else:
            zero = key

    encryption_map = dict(zip([zero, one, two, three, four, five, six, seven, eight, nine], '0123456789'))
    result = ''.join([encryption_map[frozenset(key)] for key in encryption_test])
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
