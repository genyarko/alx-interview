#!/usr/bin/env python3
'''A module for working with lockboxes.
'''

from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    Args:
        boxes (List[List[int]]): A list of boxes, where each box is represented
            as a list of integers representing the indices of other boxes it can unlock.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''

    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not (0 <= boxIdx < n):
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    
    return n == len(seen_boxes)
