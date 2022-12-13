def open_input():
    filepath = '../../resources/day04_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

if __name__ == '__main__':
    lines = open_input()
    for line in lines:
        print(line)