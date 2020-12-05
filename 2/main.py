import collections

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
        c = collections.Counter(password)
        if c[letter] >= int(min_count) and c[letter] <= int(max_count):
            response.append(password)
    
    print(len(response))

if __name__ == "__main__":
    main()