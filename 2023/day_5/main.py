def run():
    with open("input.txt") as f:
        lines = f.read().split("\n\n")

        seeds_input = lines[0]
        seeds = []
        for seed in seeds_input.split(":")[1].strip().split(" "):
            seeds.append(int(seed))

        mappings = {}
        for mapping_input in lines[1:]:
            mapping_input_parts = mapping_input.split("\n")
            mapping_input_header = mapping_input_parts[0]
            mapping_input_name = mapping_input_header.split(" ")[0]
            mapping_input_data = mapping_input_parts[1:]
            mapping_values = []
            for mapping_line in mapping_input_data:
                dst, source, _range = [int(v) for v in mapping_line.split(" ")]
                range_start = source
                range_end = source + _range - 1
                dst_start = dst
                dst_end = dst + _range - 1
                mapping_values.append((range_start, range_end, dst_start, dst_end))
            mapping_values.sort(key=lambda m: m[2])
            if mapping_values[0][2] > 0:
                range_from_zero = (
                    0,
                    mapping_values[0][2] - 1,
                    0,
                    mapping_values[0][2] - 1,
                )
                mapping_values = [range_from_zero] + mapping_values

            # (src_start, src_end, dst_start, dst_end)
            complete_ranges = [mapping_values[0]]
            i = 1
            while i < len(mapping_values):
                left = complete_ranges[-1]
                right = mapping_values[i]
                if left[3] + 1 != right[2]:
                    complete_ranges.append(
                        (left[3] + 1, right[2] - 1, left[3] + 1, right[2] - 1)
                    )
                else:
                    complete_ranges.append(right)
                    i += 1

            mappings[mapping_input_name] = complete_ranges

        # keys =
        target = 0
        for k in reversed(list(mappings.keys())):
            print(k, target)
            target = find_in_range(target, mappings[k])
        print(target)
        # print(list(mappings.keys()).reverse())
        # for k, v in mappings.items():
        #     print(k)
        #     print(v)


def find_in_range(target: int, ranges: list[tuple[int, int, int, int]]) -> int:
    for src_start, src_end, dst_start, dst_end in ranges:
        if target >= dst_start and target <= dst_end:
            delta = target - dst_start
            return src_start + delta

    return target


if __name__ == "__main__":
    run()
