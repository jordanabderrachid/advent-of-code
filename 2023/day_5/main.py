from typing import Self


class Range:
    def __init__(self, src, dst, size):
        if src < 0 or dst < 0 or size <= 0:
            raise ValueError(f"invalid {src} {dst} {size}")

        self.src_start = src
        self.src_end = src + size - 1
        self.dst_start = dst
        self.dst_end = dst + size - 1

    def __repr__(self) -> str:
        return f"({self.src_start}, {self.src_end}, {self.dst_start}, {self.dst_end})"

    def apply(self, other: Self) -> tuple[Self, list[Self]]:
        # this should return the destination of self, and compare the destination of other
        # with the source of self
        if other.dst_end < self.src_start:
            return (None, [other])

        if (
            other.dst_start < self.src_start
            and other.dst_end >= self.src_start
            and other.dst_end <= self.src_end
        ):
            remainder_size = self.src_start - other.dst_start
            remainder = Range(other.dst_start, other.dst_start, remainder_size)

            mapped = Range(
                self.dst_start, self.dst_start, other.dst_end - self.src_start + 1
            )
            return (mapped, [remainder])

        if other.dst_start >= self.src_start and other.dst_end <= self.src_end:
            offset = other.dst_start - self.src_start
            size = other.dst_end - other.dst_start + 1
            return (Range(self.dst_start + offset, self.dst_start + offset, size), [])

        if (
            other.dst_start >= self.src_start
            and other.dst_start <= self.src_end
            and other.dst_end > self.src_end
        ):
            offset = other.dst_start - self.src_start
            size = self.src_end - other.dst_start + 1
            mapped = Range(self.dst_start + offset, self.dst_start + offset, size)

            remainder_size = other.dst_end - self.src_end
            remainder = Range(
                other.src_start + size, other.src_start + size, remainder_size
            )

            return (mapped, [remainder])

        if other.dst_start > self.src_end:
            return (None, [other])

        if other.dst_start < self.src_start and other.dst_end > self.src_end:
            remainder_left_size = self.src_start - other.dst_start
            remainder_left = Range(
                other.dst_start, other.dst_start, remainder_left_size
            )

            remainder_right_size = other.dst_end - self.src_end
            remainder_right = Range(
                self.src_end + 1, self.src_end + 1, remainder_right_size
            )
            return (self, [remainder_left, remainder_right])

        raise "should not happen"


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n\n")

        seeds_input = lines[0].split(":")[1].strip().split(" ")
        seeds: list[Range] = []
        for i in range(0, len(seeds_input), 2):
            seeds.append(
                Range(int(seeds_input[i]), int(seeds_input[i]), int(seeds_input[i + 1]))
            )

        mappings: list[list[Range]] = []
        for mapping_input in lines[1:]:
            mapping_values = []
            mapping_input_parts = mapping_input.split("\n")
            mapping_input_data = mapping_input_parts[1:]

            for mapping_line in mapping_input_data:
                dst, src, size = [int(v) for v in mapping_line.split(" ")]
                mapping_values.append(Range(src, dst, size))
            mappings.append(mapping_values)

        mins = []
        for start_range in seeds:
            current_ranges = [start_range]
            for i in range(len(mappings)):
                next_ranges = []
                print(" ".join(str(r) for r in current_ranges))
                for current_range in current_ranges:
                    next_ranges += apply_ranges(current_range, mappings[i])
                current_ranges = next_ranges
            mins.append(min_from_ranges(current_ranges))
            print("---")
        print(min(mins))


def apply_ranges(current: Range, others: list[Range]) -> list[Range]:
    remainder = [current]
    res = []
    for other in others:
        next_remainder = []
        for current in remainder:
            resulting_range, rest = other.apply(current)
            if resulting_range:
                res.append(resulting_range)
            next_remainder += rest
        remainder = next_remainder

    return res + remainder


def min_from_ranges(ranges: list[Range]) -> int:
    return min([r.dst_start for r in ranges])


if __name__ == "__main__":
    run()
