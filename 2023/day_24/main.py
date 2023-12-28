import numpy as np
from itertools import combinations


def run():
    with open("input.txt") as f:
        hailstones = []
        lines = f.read().splitlines()
        for line in lines:
            p, v = line.split(" @ ")
            p = list(map(int, p.split(", ")))
            v = list(map(int, v.split(", ")))
            P = np.array(p[:-1]).reshape(2, 1)
            V = np.array(v[:-1]).reshape(2, 1)
            hailstones.append((P, V))

        res = 0
        for a, b in combinations(hailstones, 2):
            if instersect(a, b):
                res += 1

        print(res)


def instersect(a, b):
    Pa, Va = a
    Pb, Vb = b

    # Solve M@T = C
    # T is a (2, 1) matrix that contains (ta, tb)
    M = np.concatenate((Va, -Vb), axis=1)
    C = Pb - Pa
    try:
        M_inv = np.linalg.inv(M)
    except np.linalg.LinAlgError:
        return False

    T = M_inv @ C

    # checks that all t > 0
    for t in T.reshape(-1).tolist():
        if t < 0:
            return False

    # S = P + T @ V
    # P = np.concatenate((Pa, Pb))
    # V = np.concatenate((Va, Vb))
    Ta, _ = T.reshape(-1).tolist()
    x, y = (Pa + Ta * Va).reshape(-1).tolist()
    if (
        x < 200000000000000
        or x > 400000000000000
        or y < 200000000000000
        or y > 400000000000000
    ):
        return False

    return True


if __name__ == "__main__":
    run()
