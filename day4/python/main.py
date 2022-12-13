def open_input():
    filepath = '../../resources/day04_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

def parse_elves(lines):
    pairs = []
    for line in lines:
        elf_pair = [elf.split('-') for elf in line[:-1].split(',')]
        elf_pair = [(int(elf[0]), int(elf[1])) for elf in elf_pair]
        pairs.append(elf_pair)
    return pairs

def find_full_intersection(pairs : list):
    intersections = []
    for pair in pairs:
        first_pair = pair[0]
        second_pair = pair[1]
        if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]:
            intersections.append(pair)
            continue
        elif second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]:
            intersections.append(pair)
            continue
    return intersections


def find_entire_intersection(pairs : list):
    intersections = []
    for idx, pair in enumerate(pairs):
        first_pair = pair[0]
        second_pair = pair[1]
        intersection_range = []
        for section in range(first_pair[0], first_pair[1] + 1):
            for other_section in range(second_pair[0], second_pair[1] + 1):
                if section == other_section:
                    intersection_range.append(section)
        if (len(intersection_range) != 0):
            intersections.append((pair, intersection_range))
    return intersections

if __name__ == '__main__':
    lines = open_input()
    pairs = parse_elves(lines)
    intersections = find_full_intersection(pairs)
    whole_intersections = find_entire_intersection(pairs)

    print("Number of entire intersections: ", len(intersections))
    print("Number of intersections: ", len(whole_intersections))
