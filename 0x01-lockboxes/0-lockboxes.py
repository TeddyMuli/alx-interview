#!/usr/bin/env python3
"""
Python script to check if all boxes can be opened.
Return True if all boxes can be opened else return False.
"""


def canUnlockAll(boxes):
    """Function to get the number of opened boxes."""
    if (not isinstance(boxes, list) or (len(boxes) <= 0)):
        return False

    opened_boxes = set()
    opened_boxes.add(0)
    queue = [0]

    while queue:
        box_index = queue.pop(0)
        for key in boxes[box_index]:
            if ((key < len(boxes)) and (key not in opened_boxes)):
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)
