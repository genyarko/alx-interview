#!/usr/bin/python3

def canUnlockAll(boxes):
  """Determines if all the boxes can be opened.

  Args:
    boxes: A list of lists, where each inner list contains the keys to open the
      corresponding box.

  Returns:
    True if all the boxes can be opened, False otherwise.
  """

  unlocked = set([0])
  queue = [0]
  while queue:
    box = queue.pop(0)
    for key in boxes[box]:
      if key not in unlocked:
        unlocked.add(key)
        queue.append(key)
  return len(unlocked) == len(boxes)
