"""
================================================================================

  File Name: bubble.py

  Purpose: Impelmenting Bubble Sort algorithm in Python.

  Creation Date: 05-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""
import random

def bubble_sort(lst):
    """
    Sorts a given list/array using bubble sort algorithm.

    Algorithm:
    ----------
        >>> It repeated steps through the list
        >>> Compares adjacent elements and swaps them if they are in the wrong order!
        >>> With each pass throught the list, the largest unsorted element 'bubbles up'
            to its correct position.

    Parameters:
    ----------
        lst: list()
             The unordered list which needs to be sorted.
    """
    length = len(lst) # we need the length of the list!

    # Traverses through the list.
    for x in range(length):
        # Last x elements in the list is already in place!
        for j in range(0, length - 1 -x):
            # swap the element in j index if greater than the element in j+1 index!
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# creating a list of random int (numbers)
lst = [random.randint(23, 76) for _ in range(11)]
print(f"Unordered list: {lst}")

# sorting the list with the function that we just wrote above
bubble_sort(lst)
print(f"Ordered list: {lst}")
