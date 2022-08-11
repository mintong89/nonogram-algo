# Simple spaces.

def simple_spaces(clues: list[int], row: list[str]):
    '''
    # Simple spaces
    ---------------
    Method that used to eliminate spaces that out of range of any possible blocks of boxes.

    Example:
    --------
    Clues: [3, 1]
    Row: ['O', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'O']
    Result: ['-', 'O', 'X', 'X', 'O', '-', '-', 'X', '-', '-']
    '''

    boxes_of_row = list(
        map(lambda x: len(x), ''.join(row).replace('O', ' ').split()))

    # Check if boxes of row is same as clues.
    if boxes_of_row == clues:
        return row

    # check validity.

    return []


print(simple_spaces([3, 1], ['O', 'O', 'O',
      'O', 'X', 'O', 'O', 'X', 'O', 'O']))
