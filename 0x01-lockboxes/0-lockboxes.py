#!/usr/bin/env python3
'''Lockbox
'''
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if isinstance(key, int) and 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
