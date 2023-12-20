modules = {}


def run():
    with open("input.txt") as f:
        modules["output"] = Output()

        lines = f.read().splitlines()
        for line in lines:
            module = line.split("->")[0].strip()

            if module == "broadcaster":
                modules["broadcaster"] = Broadcaster()
            else:
                module_type = module[0]
                module_name = module[1:]

                if module_type == "%":
                    modules[module_name] = FlipFlop()

                if module_type == "&":
                    modules[module_name] = Conjuction()

        for line in lines:
            input_module, destination_modules = line.split("->")
            input_module = input_module.strip()
            if input_module[0] in "&%":
                input_module = input_module[1:]

            destination_modules = [v.strip() for v in destination_modules.split(",")]
            for dst in destination_modules:
                modules[input_module].add_destination(dst)

                if dst not in modules:
                    modules[dst] = Output()

                modules[dst].add_input(input_module)

        # lo_count = 0
        # hi_count = 0
        # press_count = 0
        # press = True
        # while press:
        for press_count in range(1, 11):
            # press_count += 1
            # if press_count % 100000 == 0:
            #     print(press_count)
            q = [("aptly", "broadcaster", "lo")]
            while q:
                fr, to, pulse = q.pop(0)

                if (to, pulse) == ("rx", "lo"):
                    print("ans = ", press_count)
                    # press = False
                # if pulse == "lo":
                #     lo_count += 1
                # else:
                #     hi_count += 1
                # print(f"{fr} -{pulse}-> {to}")

                for next_module, next_pulse in modules[to].pulse(fr, pulse):
                    q.append((to, next_module, next_pulse))

            print(press_count)
            for name, mod in modules.items():
                if isinstance(mod, Conjuction):
                    print(name, mod._inputs)
        # print(lo_count * hi_count)


class FlipFlop:
    def __init__(self):
        self._is_on = False
        self._destinations = []
        # self._inputs = {}

    def add_destination(self, dst):
        self._destinations.append(dst)

    def add_input(self, frm):
        pass
        # self._inputs[frm] = "lo"

    # returns list of (module_name, pulse_type)
    def pulse(self, frm, type) -> list[tuple[str, str]]:
        if type == "hi":
            return []

        if type == "lo":
            pulse_type = "lo" if self._is_on else "hi"
            self._is_on = not self._is_on
            return [(dst, pulse_type) for dst in self._destinations]


class Broadcaster:
    def __init__(self):
        self._destinations = []

    def add_destination(self, dst):
        self._destinations.append(dst)

    def add_input(self, frm):
        pass

    # returns list of (module_name, pulse_type)
    def pulse(self, frm, type) -> list[tuple[str, str]]:
        return [(dst, type) for dst in self._destinations]


class Conjuction:
    def __init__(self):
        self._destinations = []
        self._inputs = {}

    def add_destination(self, dst):
        self._destinations.append(dst)

    def add_input(self, frm):
        self._inputs[frm] = "lo"

    # returns list of (module_name, pulse_type)
    def pulse(self, frm, type) -> list[tuple[str, str]]:
        self._inputs[frm] = type

        pulse_type = "hi"
        if all([input_pulse == "hi" for input_pulse in self._inputs.values()]):
            pulse_type = "lo"

        return [(dst, pulse_type) for dst in self._destinations]


class Output:
    def __init__(self):
        pass

    def add_destination(self, dst):
        pass

    def add_input(self, frm):
        pass

    # returns list of (module_name, pulse_type)
    def pulse(self, frm, type) -> list[tuple[str, str]]:
        return []


if __name__ == "__main__":
    run()
