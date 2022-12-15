import regex

def open_input():
    filepath = '../../resources/day07_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

class File():
    def __init__(self, size, name) -> None:
        self.size = int(size)
        self.name = name
    def __str__(self) -> str:
        return f"- {self.name} (file, size={self.size})"

class Directory():
    def __init__(self, name) -> None:
        self.max_size = 70000000
        self.name = name
        self.parent = None
        self.size = None
        self.dir_childrens = {}
        self.file_childrens = []

    def get_how_many_parent(self):
        how_many_parent = 1
        parent = self.parent
        while parent != None:
            how_many_parent += 1
            parent = parent.parent
        return how_many_parent

    def __len__(self):
        if self.size != None:
            return self.size
        size = 0
        for file in self.file_childrens:
            size += file.size
        for dir in self.dir_childrens:
            size += len(self.dir_childrens[dir])
        self.size = size
        return size

    def __str__(self) -> str:
        base = f"- {self.name} (dir, size={len(self)})"
        parents = self.get_how_many_parent()
        indentation = '    ' * parents
        for dir in self.dir_childrens:
            base += f"\n{indentation}{self.dir_childrens[dir]}"
        for file in self.file_childrens:
            base += f"\n{indentation}{file}"
        return base

    def add_directory(self, directory):
        for dir in self.dir_childrens:
            if (self.dir_childrens[dir].name == directory.name):
                return
        directory.parent = self
        directory.max_size = self.max_size
        self.dir_childrens[directory.name] = directory

    def add(self, line):
        if (line.startswith("dir ")):
            dirName = line[4:]
            self.add_directory(Directory(dirName))
        if (regex.match(r"^[0-9]+", line)):
            splitted_line = line.split(" ")
            self.file_childrens.append(File(splitted_line[0], splitted_line[1]))

    def get_root(self):
        root = self
        while root.parent != None:
            root = root.parent
        return root

    def get(self, directory_name):
        if directory_name == "..":
            return self.parent
        elif directory_name == '/':
            return self.get_root()
        for dir in self.dir_childrens:
            if (self.dir_childrens[dir].name == directory_name):
                return self.dir_childrens[dir]

    def get_whole_size(self):
        size = 0
        if (len(self) <= 100000):
            size += len(self)
        for dir in self.dir_childrens:
            size += self.dir_childrens[dir].get_whole_size()
        return size

    @property
    def unused_space(self):
        return self.max_size - len(self.get_root())

    def free_space(self, size, indent = 0):
        min = self
        changed = False
        for dir in self.dir_childrens:
            current_len = len(self.dir_childrens[dir])
            possible_unused_space = self.unused_space + current_len
            indentation = '    ' * indent
            if not (possible_unused_space >= size):
                continue
            else:
                changed = True
                local_min = self.dir_childrens[dir].free_space(size, indent + 1)
                if (len(local_min) < len(min)):
                    min = local_min
        return min if changed else self


def parse_commands(lines):
    currentDir: Directory = None
    is_listing = False
    for line in lines:
        if (line.startswith("#")): continue
        line: str = line[:-1]
        is_command = line.startswith("$")
        splitted_line = line.split(" ")
        command = None if not is_command else splitted_line[1]
        if (currentDir == None):
            currentDir = Directory(line.split("cd")[-1][1:])
        if (is_listing):
            if (is_command):
                is_listing = False
            else:
                currentDir.add(line)
        if (command == 'ls'):
            is_listing = True
        elif (command == 'cd'):
            dirName = splitted_line[2]
            currentDir = currentDir.get(dirName)
    return currentDir.get_root()

if __name__ == '__main__':
    lines = open_input()
    root: Directory = parse_commands(lines)
    min_dir = root.free_space(30000000)
    print(len(min_dir))
