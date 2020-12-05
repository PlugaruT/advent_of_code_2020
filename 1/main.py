import itertools


def read_input():
    with open("input.txt") as input_file:
        lines = {int(i.strip()) for i in input_file.readlines()}
    return lines


def main():
    expenses = read_input()
    pairs = itertools.combinations(expenses, 3)
    r = list(filter(lambda x: x[0] + x[1] + x[2] == 2020, pairs))
    print(r[0][0] * r[0][1] * r[0][2])


if __name__ == "__main__":
    main()