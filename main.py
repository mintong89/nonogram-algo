# Shit Nonogram algorithm by mintong89
# ------------------------------------
# Indication:
# -----------
# -: blank, X: box, O: flag

from util import NonoBoard
from simple_boxes import simple_boxes

test = NonoBoard(10)

test.set(['O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O'], 1)

print(simple_boxes(space_size=10, clues=[4, 3]))
