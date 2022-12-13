
def open_input():
    filepath = '../../resources/day03_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

def get_priority(char):
    ascii = ord(char)
    if ascii >= 97 and ascii <= 122:
        ascii -= ord('a') - 1
    else:
        ascii -= ord('A') - 27
    return ascii

def parse_containers(lines):
    whole = 0
    for line in lines:
        line = line.replace('\n', '')
        mid = int((len(line) - 1) / 2) + 1
        left = line[:mid]
        right = line[mid:]
        for char in left:
            if char in right:
                ascii = get_priority(char)
                break
        whole += ascii
    return whole

def parse_elves_group(lines):
    whole = 0
    for i in range(0, len(lines), 3):
        first_line = lines[i].replace('\n', '')
        second_line = lines[i + 1].replace('\n', '')
        third_line = lines[i + 2].replace('\n', '')
        intersections = set(third_line).intersection(second_line).intersection(first_line)
        whole += get_priority(list(intersections)[0])
    return whole

if __name__ == '__main__':
    lines = open_input()
    per_line = parse_containers(lines)
    per_group = parse_elves_group(lines)
    print("Total of item per line: ", per_line)
    print("Total of item per group: ", per_group)