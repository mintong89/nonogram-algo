# Simple boxes.

def simple_boxes(clues: list[int], row_num: int):
    '''
    # Simple boxes
    --------------
    Method that used to determine as many boxes as possible.

    Example:
    --------
    Clues: [4, 3]
    Row Number: 10
    Result: ['O', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O']
    '''

    sum_of_clues = sum(clues)
    sum_of_clues_and_gap = sum_of_clues + len(clues) - 1

    # check validity.
    if sum_of_clues_and_gap > row_num:
        raise ValueError(
            'Sum of clues and gap between is more than row number!')

    if sum_of_clues_and_gap < row_num / 2:
        return ['O' for _ in range(row_num)]

    if sum_of_clues == row_num:
        return ['X' for _ in range(row_num)]

    # simple_boxes algo.
    combination = []
    for n in clues:
        blocks = ['X' for _ in range(n)]

        for i in range(min(n, row_num - sum_of_clues_and_gap)):
            blocks[i] = 'O'

        combination += blocks

        if (len(combination) != row_num):
            combination.append('O')

    # fill up remaining spaces.
    while (len(combination) != row_num):
        combination.append('O')

    return combination
