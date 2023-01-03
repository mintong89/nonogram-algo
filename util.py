# direction type: horizontal, vertical
# cell type: -, O, X

class NonoRow:
    def gen(space_size: int, value = '-') -> list[str]:
        return [value for _ in range(space_size)]

    def count(row: list[str]) -> list[tuple]:
        result: list[tuple] = []

        count = 0
        start_index = 0
        for i in range(len(row)):
            if row[i] == 'X':
                if count == 0:
                    start_index = i

                count += 1
            elif count > 0:
                result.append((start_index, count))

                count = 0

        return result

class NonoBoard:
    def __init__(self, space_size: int) -> None:
        self.space_size = space_size
        self.board = [NonoRow.gen(self.space_size) for _ in range(space_size)]
    
        print('The nonogram board has created with the size of {}x{}.'.format(space_size, space_size))

    def get(self, index: int, direction: str = 'horizontal') -> list[str]:
        if index < 0 or index > self.space_size:
            raise IndexError('The index should within space size')

        return self.board[index] if direction == 'horizontal' else [r[index] for r in self.board]
    
    def get_count(self, index: int, direction: str = 'horizontal') -> list[tuple]:
        return NonoRow.count(self.get(index, direction))

    def set(self, row: list[str], index: int, direction: str = 'horizontal') -> list:
        if len(row) != self.space_size:
            raise ValueError('Amount of values provided is not same as space size.')

        if not set(row) <= {'-', 'O', 'X'}:
            raise ValueError('Only value of X, O or - is accepted.')

        if direction == 'horizontal':
            self.board[index] = row
        else:
            for i in range(self.space_size):
                self.board[index][i] = row[i]

        return self.board[index]

    def __str__(self) -> str:
        return '\n'.join([str(x) for x in self.board])

    