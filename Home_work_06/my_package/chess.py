__all__ = ['chess']

import sys


def is_safe(board, row, col):
    for i in range(row):
        # Проверяем бьют ли ферзи друг друга по вертикали или диагонали
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def find_safe_arrangements(board, row=0, count=4, results=None):
    if results is None:
        results = []

    if row == 8 or len(results) >= count:
        return results

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if row == 7:
                results.append(board[:])
                if len(results) >= count:
                    return results
            else:
                results = find_safe_arrangements(board, row + 1, count, results)

    return results


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("K ", end="")
            else:
                print("0 ", end="")
        print()


def main():
    if len(sys.argv) == 2:
        count = int(sys.argv[1])
    else:
        count = 4

    # Инициализация пустой расстановки ферзей
    queens = [0] * 8

    # Поиск и вывод заданного количества безопасных расстановок ферзей
    safe_arrangements = find_safe_arrangements(queens, count=count)

    if safe_arrangements:
        print(f"Найдены следующие {count} безопасные расстановки ферзей:")
        for arrangement in safe_arrangements:
            print_board(arrangement)
            print()
    else:
        print("Нет безопасных расстановок ферзей.")


if __name__ == "__main__":
    main()
