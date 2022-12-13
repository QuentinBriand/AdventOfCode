def open_input():
    filepath = '../../resources/day05_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

class Ship():
    def __init__(self, lines, version) -> None:
        self.hold = []
        self.max_length = 0
        self.version = version
        self.get_containers(lines)
        for container in self.hold:
            self.max_length = max(self.max_length, len(container))

    def get_tops(self):
        for container in self.hold:
            print(container[container.count(' ')], end='')
        print()

    def process_directions(self, lines):
        for line in lines:
            line: str = line[:-1]
            if not (line.startswith('move')):
                continue
            directions = line.split(' ')
            nbr_items = int(directions[1])
            from_container = self.hold[int(directions[3]) - 1]
            to_container = self.hold[int(directions[5]) - 1]
            letters = self.take_from(from_container, nbr_items)
            letters = letters if self.version == 9000 else letters[::-1]
            for letter in letters:
                self.add_to(letter, to_container)


    def add_to(self, letter, container):
        idx = container.count(' ')
        if (idx == 0):
            self.max_length += 1
            for o_container in self.hold:
                o_container.insert(0, ' ')
            container[idx] = letter
        else:
            container[idx - 1] = letter


    def take_from(self, container, count):
        idx = container.count(' ')
        letters = []
        for i in range(count):
            new_letter = container[idx + i]
            letters.append(new_letter)
            container[idx + i] = ' '
        return letters


    def display_hold(self):
        for i in range(self.max_length):
            for container in self.hold:
                if (container[i] != ' '):
                    print(f'[{container[i]}]', end=' ')
                else: print('    ', end='')
            print()
        for i in range(len(self.hold)):
            print(f' {i + 1}  ', end='')
        print()


    def get_containers(self, lines):
        containers = []
        for line in lines:
            if (line.startswith('[')):
                line = line[:-1]
                container_index = 0
                for i in range(0, len(line), 4):
                    self.add_to_container(line[i + 1 : i + 2], container_index)
                    container_index += 1
        return containers


    def add_to_container(self, letter, container_index):
        if len(self.hold) <= container_index:
            self.hold.append([])
        self.hold[container_index].append(letter)

if __name__ == '__main__':
    lines = open_input()
    ship: Ship = Ship(lines, 9001)
    ship.display_hold()
    ship.process_directions(lines[ship.max_length:])
    ship.display_hold()
    ship.get_tops()