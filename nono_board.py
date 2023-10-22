from typing import Literal, overload


class NonoValue:
    EMPTY = 0
    FILLED = 1
    VOID = -1
    NONOTYPE = Literal[0, 1, -1]


class NonoList:
    def _check_list_sizes(self, list_1, list_2):
        if len(list_1) != len(list_2):
            raise ValueError('Lists are not in same size.')

    @overload
    def __init__(self, size: int):
        ...

    @overload
    def __init__(self, values: list[NonoValue.NONOTYPE]):
        ...

    def __init__(self, *args):
        if isinstance(args[0], int):
            self.values = [NonoValue.EMPTY for _ in range(args[0])]
        elif isinstance(args[0], list):
            self.values: list[int] = args[0]

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def __getitem__(self, index: int):
        return self.values[index]

    def __setitem__(self, index: int, value: NonoValue.NONOTYPE):
        self.values[index] = value

    def __add__(self, other):
        self._check_list_sizes(self, other)

        result = []

        for i in range(len(self)):
            if self[i] == NonoValue.FILLED and other[i] == NonoValue.VOID or self[i] == NonoValue.VOID and other[i] == NonoValue.FILLED:
                raise ValueError(
                    f'On row {i} expected any one is empty field but contain conflict values.')

            if self[i] == NonoValue.VOID or other[i] == NonoValue.VOID:
                result.append(NonoValue.VOID)
            elif self[i] == NonoValue.FILLED or other[i] == NonoValue.FILLED:
                result.append(NonoValue.FILLED)
            else:
                result.append(NonoValue.EMPTY)

        return NonoList(result)

    def starts(self):
        return [index for index, value in enumerate(self.values) if (index == 0 or self.values[index - 1] != NonoValue.FILLED) and value == NonoValue.FILLED]

    def ends(self):
        return [index + 1 for index, value in enumerate(self.values) if (index == len(self) - 1 or self.values[index + 1] != NonoValue.FILLED) and value == NonoValue.FILLED]

    def counts(self):
        return list(map(int.__sub__, self.ends(), self.starts()))

    def gaps(self):
        starts = self.starts()
        ends = self.ends()

        result: list[int] = []

        for index, value in enumerate(starts):
            if index == 0 and value != 0:
                result.append(value)
            else:
                if index == (len(starts) - 1) and ends[index] != len(self) - 1:
                    if len(self) - ends[index] != 0:
                        result.append(len(self) - ends[index])

                    continue

                result.append(starts[index + 1] - ends[index])

        return result

    def __str__(self):
        return str(self.values)


class NonoBoard:
    def _check_index(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError

    def _check_size(self, values: NonoList):
        if len(values) != self.size:
            raise ValueError(
                f'Expected size of {self.size} but getting {len(values)}.')

    def __init__(self, size: int):
        self.space = [[NonoValue.EMPTY for _ in range(
            size)] for _ in range(size)]
        self.size = size

    def set_row(self, index: int, values: NonoList):
        self._check_index(index)
        self._check_size(values)

        self.space[index] = list(values)

    def set_col(self, index: int, values: NonoList):
        self._check_index(index)
        self._check_size(values)

        for i in range(self.size):
            self.space[i][index] = values[i]

    def set_cell(self, row: int, col: int, value: NonoValue.NONOTYPE):
        self.space[row][col] = value

    def get_row(self, index: int):
        self._check_index(index)

        return NonoList(self.space[index])

    def get_col(self, index: int):
        self._check_index(index)

        return NonoList([row[index] for row in self.space])

    def get_cell(self, row: int, col: int):
        return self.space[row][col]

    def __str__(self):
        return '\n'.join([str(row) for row in self.space])
