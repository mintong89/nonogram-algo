from nono_board import NonoList, NonoValue


def simple_boxes(size: int, clues: list[int]):
    smallest_possible_blocks = sum(clues) + len(clues) - 1

    if smallest_possible_blocks <= size / 2:
        return NonoList(size)

    offset = [NonoValue.EMPTY for _ in range(size - smallest_possible_blocks)]

    temp: list[NonoValue.NONOTYPE] = []
    for index, clue in enumerate(clues):
        temp += [NonoValue.FILLED for _ in range(clue)]
        if index != len(clues) - 1:
            temp.append(NonoValue.EMPTY)

    return NonoList(list(map(lambda l, r: NonoValue.FILLED if l == NonoValue.FILLED and l == r else NonoValue.EMPTY, temp + offset, offset + temp)))
