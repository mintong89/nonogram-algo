# Shit Nonogram algorithm by mintong89
# ------------------------------------
# Indication:
# -----------
# -: blank, X: box, O: flag

from util import NonoBoard

test = NonoBoard(10)

test.set(['O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O'], 0)

print(test.get(0, 'vertical'))
