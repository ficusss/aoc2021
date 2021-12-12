import sys


TInputLine = tuple[tuple[str, str, str, str, str, str, str, str, str, str], tuple[str, str, str, str]]


def main():
    encryptions  = parse_input_data(sys.argv[1])


    # part1
    decode_group = [s for encrypt in encryptions for s in encrypt[1] if len(s) in [2,3,4,7]]
    print(
        f"Counting only digits in the output values, there are {len(decode_group)} " \
        "instances of digits that use a unique number of segments."
    )


def parse_input_data(filepath: str) -> list[TInputLine]:
    result = []
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            unique_signal_patterns, output_values = (elem.strip() for elem in line.split("|"))
            unique_signal_patterns, output_values = tuple(unique_signal_patterns.split()), tuple(output_values.split())
            result.append((unique_signal_patterns, output_values))

    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
