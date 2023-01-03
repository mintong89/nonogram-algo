from util import NonoRow

# X X X X - X X X - -
# - X X X X - X X X -
# - - X X X X - X X X

# result:
# - - X X - - - X - -


def simple_boxes(space_size: int, clues: list[int]) -> list[str]:
    '''
    #### Example:
    Space size: 10
    Clues: [4, 3]

    Result: - - X X - - - X - -
    '''

    sum_of_clues = sum(clues)
    sum_of_clues_and_gap = sum_of_clues + len(clues) - 1

    if sum_of_clues_and_gap > space_size:
        raise ValueError(
            'Sum of clues and gap between is more than row number!')

    # return original row if the total sum of clues is not larger than space size.
    if sum_of_clues <= space_size / 2:
        return NonoRow.gen(space_size=space_size)

    # return full if sum of clues is same as space size.
    if sum_of_clues == space_size:
        return NonoRow.gen(space_size=space_size, value='X')

    # create temp row.
    temp_row = []
    for c in clues:
        for _ in range(c):
            temp_row.append('X')

        if len(temp_row) != space_size:
            temp_row.append('-')

    while len(temp_row) < space_size:
        temp_row.append('-')

    # create combination.
    combination = []
    while True:
        combination.append(temp_row)

        if temp_row[-1] != '-':
            break

        temp_row = temp_row[:len(temp_row) - 1]
        temp_row.insert(0, '-')

    final_row = [('-' if '-' in x else 'X') for x in [[v[i]
                                                       for v in combination] for i in range(space_size)]]
    return final_row
