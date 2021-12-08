import sys
import numpy as np


def main():
    numbers, boards = parse_input_data(sys.argv[1])    

    # part1
    best_board_number, sum_all_unmarked_numbers, just_called_number = find_best_board_for_bingo(numbers, boards)
    print(f'The number of best board is {best_board_number}, ' \
        f'the sum of all unmarked numbers is {sum_all_unmarked_numbers}, ' \
        f'the number that was just called is {just_called_number}.\n' \
        f'The final score is {sum_all_unmarked_numbers * just_called_number}'
    )

    # part2
    loser_board_number, sum_all_unmarked_numbers, just_called_number = find_loser_board_for_bingo(numbers, boards)
    print(f'The number of loser board is {loser_board_number}, ' \
        f'the sum of all unmarked numbers is {sum_all_unmarked_numbers}, ' \
        f'the number that was just called is {just_called_number}.\n' \
        f'The final score is {sum_all_unmarked_numbers * just_called_number}'
    )


def parse_input_data(filepath: str) -> tuple[list[int], list[np.ndarray]]:

    with open(filepath, 'r') as fp:
        numbers = [int(n) for n in fp.readline().strip().split(',')]
        matrix_buffer = []
        boards = []
        for line in fp.readlines():
            line = line.strip()
            if not line and matrix_buffer:
                boards.append(
                    np.array(matrix_buffer)
                )
                matrix_buffer = []
            if not line:
                continue
            matrix_buffer.append([int(n) for n in line.split()])
        boards.append(np.array(matrix_buffer))

    return numbers, boards


def find_best_board_for_bingo(numbers: list[int], boards: list[np.ndarray]) -> tuple[int, int, int]:
    """
    Return: best_board_number, sum_all_unmarked_numbers, just_called_number
    """
    for called_number in numbers:
        for board_number in range(len(boards)):
            boards[board_number] = np.where(
                boards[board_number]==called_number,
                -1, boards[board_number]
            )
            column_sums = boards[board_number].sum(axis=0)
            row_sums = boards[board_number].sum(axis=1)
            if np.any(column_sums==-5) or np.any(row_sums==-5):
                best_board = np.where(
                    boards[board_number]==-1,
                    0, boards[board_number]
                )
                sum_all_unmarked_numbers = best_board.sum().sum()
                return board_number, sum_all_unmarked_numbers, called_number
    return -1, -1, -1


def find_loser_board_for_bingo(numbers: list[int], boards: list[np.ndarray]) -> tuple[int, int, int]:
    """
    Return: loser_board_number, sum_all_unmarked_numbers, just_called_number
    """
    win_boards = []
    for called_number in numbers:
        for board_number in range(len(boards)):
            if board_number in win_boards:
                continue

            boards[board_number] = np.where(
                boards[board_number]==called_number,
                -1, boards[board_number]
            )
            column_sums = boards[board_number].sum(axis=0)
            row_sums = boards[board_number].sum(axis=1)
            if np.any(column_sums==-5) or np.any(row_sums==-5):
                win_boards.append(board_number)

            if len(boards) == len(win_boards):
                loser_board = np.where(
                    boards[board_number]==-1,
                    0, boards[board_number]
                )
                sum_all_unmarked_numbers = loser_board.sum().sum()
                return board_number, sum_all_unmarked_numbers, called_number
    return -1, -1, -1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Use: python main.py input_file.txt", file=sys.stderr)
        exit()
    main()
