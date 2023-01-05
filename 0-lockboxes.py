def canUnlockAll(boxes):
    to_unlock = {0: 0}
    for i in range(1, len(boxes)):
        to_unlock[i] = None

    for box in to_unlock.keys():
        if to_unlock[box] is not None:
            for key in boxes[box]:
                to_unlock[key] = key
                if key < box:
                    for back in boxes[key]:
                        to_unlock[back] = back
    return (set(range(1, len(boxes))).issubset(set(to_unlock.values())))
