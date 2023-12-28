from collections import defaultdict


def run():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = []
        for line in lines:
            grid.append(list(line))

        # finds the start and end coords.
        start = (0, 0)
        end = (0, 0)
        for j in range(len(grid[0])):
            if grid[0][j] == ".":
                start = (0, j)

            if grid[-1][j] == ".":
                end = (len(grid) - 1, j)

        print(start, end)

        graph = defaultdict(dict)

        x_max = len(grid)
        y_max = len(grid[0])

        # build the adjency list, alonside the number of steps
        for x in range(x_max):
            for y in range(y_max):
                if grid[x][y] != "#":
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= x_max or y < 0 or y >= y_max:
                            continue

                        if grid[nx][ny] == "#":
                            continue

                        node = coord_to_str(x, y)
                        neighbor = coord_to_str(nx, ny)
                        graph[node][neighbor] = 1
                        graph[neighbor][node] = 1

        # reduces the size of the adjency list by removing trivial nodes
        for x in range(x_max):
            for y in range(y_max):
                c = coord_to_str(x, y)
                if len(graph[c].keys()) == 2:
                    neighbors = list(graph[c].keys())
                    left = neighbors[0]
                    n = graph[c][left]
                    right = neighbors[1]
                    m = graph[c][right]

                    graph[c] = dict()
                    del graph[left][c]
                    del graph[right][c]

                    graph[left][right] = n + m
                    graph[right][left] = n + m
        keys_to_del = []
        for k in graph.keys():
            if len(graph[k]) == 0:
                keys_to_del.append(k)

        for k in keys_to_del:
            del graph[k]

        res = []
        s = [(start, set(), 0)]

        while s:
            pos, visited, count = s.pop()

            if pos in visited:
                continue

            visited.add(pos)
            if pos == end:
                res.append(count)
                continue

            for neighbor, distance in graph[coord_to_str(pos[0], pos[1])].items():
                s.append((str_to_coord(neighbor), visited.copy(), count + distance))

        print(res)
        print(max(res))


def coord_to_str(x, y):
    return str(x) + ":" + str(y)


def str_to_coord(v: str):
    x, y = v.split(":")
    return (int(x), int(y))


if __name__ == "__main__":
    run()
