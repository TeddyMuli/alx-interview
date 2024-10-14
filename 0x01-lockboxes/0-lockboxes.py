#!/usr/bin/python3
"""
Python script to check if all boxes can be opened.
Return True if all boxes can be opened else return False.
"""
def canUnlockAll(boxes):
  box_num = 0
  opened_boxes = set()
  opened_boxes.add(0)

  if ((type(boxes) is not list) or (len(boxes) <= 0)):
    return False
  
  for box in boxes:
    for key in boxes[box_num]:
      if ((key < len(boxes)) and (key not in opened_boxes)):
        opened_boxes.add(key)
        box_num = key

  return len(opened_boxes) == len(boxes)
