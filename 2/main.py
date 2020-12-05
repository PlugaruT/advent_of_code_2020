def read_input():
    with open("input.txt") as input_file:
        lines = {i.strip() for i in input_file.readlines()}
    return lines


def main():
    passwords = read_input()
    response = []
    for line in passwords:
        policy, password = line.split(":")
        counts, letter = policy.split(" ")
        min_count, max_count = counts.split("-")
        password = password.strip()
        if password[int(min_count) - 1] == letter and not password[int(max_count) - 1] == letter:
            response.append(password)

        if password[int(max_count) - 1] == letter and not password[int(min_count) - 1] == letter:
            response.append(password)

    print(len(response))


if __name__ == "__main__":
    main()