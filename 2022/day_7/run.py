import re

from shared.input import read_input

class Sizeable:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_size(self) -> int:
        pass

class Directory(Sizeable):
    def __init__(self, name: str, parent = None) -> None:
        super().__init__(name)
        self.content = []
        if parent is None:
            self.parent = self
        else:
            self.parent = parent

    def append(self, content: Sizeable) -> None:
        self.content.append(content)

    def get_size(self) -> int:
        return sum(c.get_size() for c in self.content)

    def get_all_sizes(self):
        sizes = [self.get_size()]
        for subdir in self.get_subdirs():
            for size in subdir.get_all_sizes():
                sizes.append(size)

        return sizes

    def get_parent(self):
        return self.parent

    def get_subdirs(self):
        return filter(lambda d: isinstance(d, Directory), self.content)

    def get_dir(self, name):
        try:
            return next(d for d in self.get_subdirs() if d.name == name)
        except StopIteration:
            print("{} dir does not contain {}".format(self.name, name))
            raise SystemExit

class File(Sizeable):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.size = size

    def get_size(self) -> int:
        return self.size

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("/")
        self.current = self.root

    def cd(self, dir: str) -> None:
        # print("cd {}".format(dir))
        match dir:
            case "/":
                self.current = self.root
            case "..":
                self.current = self.current.get_parent()
            case _:
                self.current = self.current.get_dir(dir)
    
    def mkdir(self, name: str):
        # print("mkdir {}".format(name))
        self.current.append(Directory(name, self.current))

    def touch(self, name: str, size: int):
        # print("touch {} {}".format(name, size))
        self.current.append(File(name, size))

cd_matcher = re.compile("^\$ cd (.+)$")
file_matcher = re.compile("^(\d+) (.+)$")
dir_matcher = re.compile("^dir (.+)$")

def run():
    fs = FileSystem()
    f = read_input("day_7")
    lines = f.split("\n")
    for l in lines:
        result = cd_matcher.search(l)
        if result is not None:
            fs.cd(result.group(1))
            continue

        if l == "$ ls":
            continue

        result = file_matcher.search(l)
        if result is not None:
            fs.touch(result.group(2), int(result.group(1)))
            continue

        result = dir_matcher.search(l)
        if result is not None:
            fs.mkdir(result.group(1))
            continue

        print(l)
        raise SystemExit

    sizes = fs.root.get_all_sizes()
    print(sorted(sizes))
    print("done")