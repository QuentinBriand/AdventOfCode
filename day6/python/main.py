from enum import Enum

def open_input():
    filepath = '../../resources/day06_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

class StartOf(Enum):
    PACKET = 4
    MESSAGE = 14

def find_start_of_packet(line, start_of_type : StartOf):
    start_of_packet = ""
    max_length = len(line) - start_of_type.value
    for i in range(max_length):
        start_of_packet = line[i:i + start_of_type.value]
        if len(set(start_of_packet)) == start_of_type.value:
            return i + start_of_type.value

if __name__ == '__main__':
    lines = open_input()
    for line in lines:
        start_of = find_start_of_packet(line[:-1], StartOf.MESSAGE)
        print("Marker appears after the {}th character".format(start_of))