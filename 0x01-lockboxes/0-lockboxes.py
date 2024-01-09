#!/usr/bin/python3
"""
Solve Lockboxes problem
"""


def canUnlockAll(boxes):
    """A function that determines if all the boxes can be opened"""
    if not boxes or not boxes[0]:
        return False

    boxesNum = len(boxes)
    opened = [False] * boxesNum
    opened[0] = True

    queue = [0]

    while queue:
        currentBox = queue.pop(0)

        for key in boxes[currentBox]:
            if 0 <= key < boxesNum and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
