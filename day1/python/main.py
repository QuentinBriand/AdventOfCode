
class Elf():
    def __init__(self, _foods: list):
        self._foods = _foods

    @property
    def foods(self):
        return self._foods

    @foods.setter
    def foods(self, _foods):
        self._foods = _foods

    @property
    def total(self):
        return sum(self.foods)

def open_file():
    filepath = '../../resources/day01_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

def create_elves():
    elves = []

    inventory: list = []
    for line in lines:
        if (len(line) != 1):
            inventory.append(int(line))
        else:
            elves.append(Elf(inventory))
            inventory = []
    elves.sort(key=lambda x: x.total, reverse=True)
    return elves

if __name__ == '__main__':
    lines = open_file()
    elves = create_elves()
    maximum = int(input("What is the top you want to search for ?\n"))
    for elf in elves[:maximum]:
        print(elf.total)
    whole_calories = sum(
        [elf.total for elf in elves[:maximum]]
    )
    print(f"Total elves: {len(elves)}\nTotal calories: {whole_calories}")
    #     print(f"{elf.total} - {elf.foods}")