from collections import defaultdict
from typing import Optional


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        graph, start = parse_input(lines)

        s = len(lines)
        visited = set()
        q = [(start, 0)]
        res = 0
        while q:
            node, steps = q.pop(0)
            i, j = coord(node)
            if i < 0 or i >= s or j < 0 or j >= s:
                continue

            if node in visited:
                continue

            visited.add(node)
            res = max(res, steps)
            for neighbor in graph[node]:
                q.append((neighbor, steps + 1))

        print(res)


def coord(v: str) -> (int, int):
    s = v.split(":")
    return (int(s[0]), int(s[1]))


def get_value(i: int, j: int, lines: list[str]) -> Optional[str]:
    s = len(lines)
    if i < 0 or i >= s or j < 0 or j >= s:
        return None

    return lines[i][j]


def parse_input(lines: list[str]) -> (dict, str):
    start = ""
    graph = defaultdict(set)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            curr = coords_str(i, j)
            if c == "|":
                north = get_value(i - 1, j, lines)
                if north in ["S", "|", "7", "F"]:
                    fr, to = coords_str(i - 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                south = get_value(i + 1, j, lines)
                if south in ["S", "|", "J", "L"]:
                    fr, to = coords_str(i + 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "-":
                west = get_value(i, j - 1, lines)
                if west in ["S", "-", "L", "F"]:
                    fr, to = coords_str(i, j - 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                east = get_value(i, j + 1, lines)
                if east in ["S", "-", "J", "7"]:
                    fr, to = coords_str(i, j + 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "L":
                north = get_value(i - 1, j, lines)
                if north in ["S", "|", "7", "F"]:
                    fr, to = coords_str(i - 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                east = get_value(i, j + 1, lines)
                if east in ["S", "-", "J", "7"]:
                    fr, to = coords_str(i, j + 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "J":
                north = get_value(i - 1, j, lines)
                if north in ["S", "|", "7", "F"]:
                    fr, to = coords_str(i - 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                west = get_value(i, j - 1, lines)
                if west in ["S", "-", "L", "F"]:
                    fr, to = coords_str(i, j - 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "7":
                south = get_value(i + 1, j, lines)
                if south in ["S", "|", "J", "L"]:
                    fr, to = coords_str(i + 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                west = get_value(i, j - 1, lines)
                if west in ["S", "-", "L", "F"]:
                    fr, to = coords_str(i, j - 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "F":
                south = get_value(i + 1, j, lines)
                if south in ["S", "|", "J", "L"]:
                    fr, to = coords_str(i + 1, j), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

                east = get_value(i, j + 1, lines)
                if east in ["S", "-", "J", "7"]:
                    fr, to = coords_str(i, j + 1), curr
                    graph[fr].add(to)
                    graph[to].add(fr)

            if c == "S":
                start = coords_str(i, j)

    return graph, start


def coords_str(i: int, j: int) -> str:
    return f"{i}:{j}"


if __name__ == "__main__":
    run()
