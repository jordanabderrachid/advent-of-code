def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        times = []
        for v in lines[0].split(":")[1].strip().split(" "):
            if v != "":
                times.append(v)
        distances = []
        for v in lines[1].split(":")[1].strip().split(" "):
            if v != "":
                distances.append(v)

        time = int("".join(times))
        distance = int("".join(distances))

        # res = 1
        # for i in range(len(times)):
        # time, distance = times[i], distances[i]
        c = 0
        for t in range(0, time + 1):
            speed = t
            time_travelled = time - t
            distance_travelled = time_travelled * speed
            if distance_travelled >= distance:
                c += 1

            # res *= c
        print(c)


if __name__ == "__main__":
    run()
