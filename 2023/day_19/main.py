import re

rules = {}


def run():
    with open("input.txt") as f:
        rules_str, parts_str = f.read().split("\n\n")
        for rule_str in rules_str.split("\n"):
            pattern = re.compile(r"([a-z]+)\{(.+)\}")
            match = pattern.match(rule_str)
            name, description = match.group(1), match.group(2)
            rules[name] = Rule(description)

        p = Part()
        accepted = []
        q = [(p, ["in"])]
        while q:
            part, path = q.pop(0)
            current = path[-1]
            if current == "A":
                accepted.append((part, path))
                continue

            if current == "R":
                continue

            for next_part, next_node in rules[current](part):
                q.append((next_part, path + [next_node]))

        res = 0
        for acc in accepted:
            res += acc[0].sol_cardinal()
            print(acc, acc[0].sol_cardinal())
        print(res)


class Part:
    def __init__(
        self, data={"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    ):
        self.data = data

    def __repr__(self):
        s = []
        for k, v in self.data.items():
            s.append(f"{k} {v[0]} - {v[1]}")

        return " | ".join(s)

    def copy(self):
        return Part(self.data)

    def __call__(self, condition):
        new_data = self.data.copy()
        _min, _max = new_data[condition.key]
        if condition.comp == "<":
            new_data[condition.key] = (_min, condition.value - 1)

        if condition.comp == ">":
            new_data[condition.key] = (condition.value + 1, _max)

        return Part(new_data)

    def sol_cardinal(self):
        res = 1
        for _, v in self.data.items():
            res *= v[1] - v[0] + 1

        return res


class Condition:
    def __init__(self, spec):
        pattern = re.compile(r"([a-z]{1})(<|>)(\d+)")
        match = pattern.match(spec)
        self.key = match.group(1)
        self.comp = match.group(2)
        self.value = int(match.group(3))

    def __repr__(self):
        return f"{self.key}{self.comp}{self.value}"

    def negate(self):
        if self.comp == "<":
            return Condition(f"{self.key}>{self.value-1}")

        if self.comp == ">":
            return Condition(f"{self.key}<{self.value+1}")


class Rule:
    def __init__(self, desc):
        # list of conditions + destination
        self._routes = []
        conditions = []
        for route in desc.split(","):
            if ":" not in route:
                self._routes.append((conditions, route))
            else:
                cond_desc, dest = route.split(":")
                cond = Condition(cond_desc)
                self._routes.append((conditions.copy() + [cond], dest))
                conditions.append(cond.negate())

    def __repr__(self):
        s = []
        for route in self._routes:
            conditions, dst = route
            s.append(" AND ".join([str(cond) for cond in conditions]) + " -> " + dst)

        return "\n".join(s)

    def __call__(self, part):
        res = []
        for conditions, dest in self._routes:
            new_part = part.copy()
            for cond in conditions:
                new_part = new_part(cond)
            res.append((new_part, dest))

        return res


#         for rule_str in rules_str.split("\n"):
#             pattern = re.compile(r"([a-z]+)\{(.+)\}")
#             match = pattern.match(rule_str)
#             name, description = match.group(1), match.group(2)
#             rules[name] = Rule(description)

#         rules["A"] = lambda p: "A"
#         rules["R"] = lambda p: "R"

#         accepted = []
#         rejected = []
#         for part_str in parts_str.split("\n"):
#             part = Part(part_str)
#             res = rules["in"](part)
#             if res == "A":
#                 accepted.append(part)

#             if res == "R":
#                 rejected.append(part)

#         print(sum([p.ratings() for p in accepted]))


# class Predicate:
#     def __init__(self, description: str):
#         if ":" in description:
#             spec, dest = description.split(":")
#             self.destination = dest

#             pattern = re.compile(r"([a-z]{1})(<|>)(\d+)")
#             match = pattern.match(spec)
#             key = match.group(1)
#             comp = match.group(2)
#             value = int(match.group(3))

#             if comp == "<":
#                 self._pred = lambda p: p.data[key] < value

#             if comp == ">":
#                 self._pred = lambda p: p.data[key] > value

#         else:
#             self.destination = description
#             self._pred = lambda p: True

#     def __call__(self, part):
#         if self._pred(part):
#             return self.destination

#         return None


# class Rule:
#     def __init__(self, description):
#         self._predicates = []
#         for desc in description.split(","):
#             self._predicates.append(Predicate(desc))

#     def __call__(self, part):
#         for pred in self._predicates:
#             pred_res = pred(part)
#             if pred_res is not None:
#                 return rules[pred_res](part)


# class Part:
#     def __init__(self, description) -> None:
#         self.data = {}
#         for kv in description[1:-1].split(","):
#             key, value = kv.split("=")
#             self.data[key] = int(value)

#     def ratings(self) -> int:
#         return sum(self.data.values())


if __name__ == "__main__":
    run()
