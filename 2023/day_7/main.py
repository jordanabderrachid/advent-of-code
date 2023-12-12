from collections import Counter


def run():
    with open("input.txt") as f:
        lines = f.read().split("\n")
        hands = []
        for line in lines:
            hand, bid = line.split(" ")
            hands.append((hand, int(bid), score(hand)))

        hands = sorted(hands, key=lambda h: h[2])
        print(sum([(i + 1) * h[1] for i, h in enumerate(hands)]))


card_value = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

base = 13


def score_kind(hand: str) -> int:
    counter = Counter(hand)
    if len(set(hand)) == 1:
        # print("five of a kind")
        return 6 * base**5

    if len(set(hand)) == 2 and 4 in counter.values():
        # print("four of a kind")
        return 5 * base**5

    if len(set(hand)) == 2 and 3 in counter.values() and 2 in counter.values():
        # print("full house")
        return 4 * base**5

    if len(set(hand)) == 3 and 3 in counter.values():
        # print("three of a kind")
        return 3 * base**5

    if len(set(hand)) == 3 and 2 in counter.values():
        # print("two pair")
        return 2 * base**5

    if len(set(hand)) == 4:
        # print("one pair")
        return base**5

    return 0


def score_kind_joker(hand: str) -> int:
    scores = []
    for replacement in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
        scores.append(score_kind(hand.replace("J", replacement)))

    return max(scores)


def score(hand: str) -> int:
    score = 0

    score += score_kind_joker(hand)

    for i, c in enumerate(hand):
        score += card_value[c] * base ** (4 - i)

    return score


if __name__ == "__main__":
    run()
