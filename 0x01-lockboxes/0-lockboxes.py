#!/usr/bin/python3
"""lockboxes solution"""


def canUnlockAll(boxes):
    """return true if all boxes can be unlocked"""
    s = {0}.union(set(boxes[0]))
    for box in range(0, len(boxes)):
        if box in s:
            for i in boxes[box]:
                s = s.union(set(boxes[i]))
    return set(range(1, len(boxes))).issubset(s)
