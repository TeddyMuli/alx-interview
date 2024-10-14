#!/usr/bin/python3
"""
Python script to check if all boxes can be opened.
Return True if all boxes can be opened else return False.
"""
def canUnlockAll(boxes):
  list_length = len(boxes)
  opened_boxes = [0]
  keys = set(opened_boxes)

  if ((type(boxes) is not list) or (list_length <= 0)):
    return False
  
  for box_index in opened_boxes:    
    for key in boxes[box_index]:
      if ((key <= list_length) and (key not in opened_boxes)):
        opened_boxes.append(key)
        keys.add(key)

  return len(keys) == list_length
