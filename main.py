
from techniques import simple_boxes
from nono_board import NonoBoard, NonoList


test1 = NonoList([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
test2 = NonoList([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])

print(test1 + test2)
