#!/usr/bin/env python3
"""
Python script to check if all boxes can be opened.
Return True if all boxes can be opened else return False.
"""
def canUnlockAll(boxes):
  list_length = len(boxes)
  count = 1
  box_num = 0
  opened_boxes = []

  if ((type(boxes) is not list) or (list_length <= 0)):
    return False

  for x in boxes[box_num]:
    if ((x <= list_length) and (x not in opened_boxes)):
      opened_boxes.append(x)
      box_num = x
      count += 1

  return True if count == list_length else False
