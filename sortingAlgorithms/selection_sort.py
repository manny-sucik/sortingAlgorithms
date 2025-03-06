"""
================================================================================

  File Name: selection_sort.py

  Purpose: Implementing the selection sort algorithm in Python.

  Creation Date: 06-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""

import random

def selection_sort(lst):
    """
    Sorts a list in ascendingg order using the selection sort algorithm.

    The selection sort algorithm divides the list into two parts:
        1 - A sorted part, the beginning of the list.
        2 - A unsorted part, the rest of the list.
    It repeatedly selects the smallest element from the unsorted part and swaps it
    with the first elemtn of the unsorted part, thereby increasing/growing the sorted
    list one by one.

    Algorithm:
    ---------
        >>> For each index 'x' in the list 
            - Assume that the element at index x is the smallest in the unsorted portion.
            - Iterate over the rest of the list to find the actual smalleste element.
            - If a smallest element if found, record its index!
        >>> Once the smallest element in the unsorted portion of the list is found, swap
            it with the element at index x.
        >>> Continue this process until the entire list is sorted.

    Parameters:
    -----------
        lst: list()
                The list of elements to be sorted.

    Returns:
    --------
        None: This function does not reutrn anything, since the algorithm going to change the
        list inplace.

    """

    length = len(lst)
    for x in range(length):
        # Assume the element at index x in the smallest in the unsorted part!
        smallest = x
        # check the rest of the list to find if any element is smaller.
        for j in range(x + 1, length):
            if lst[j] < lst[smallest]:
                smallest = j
        # swap the smallest found element with the element at position x
        lst[x], lst[smallest] = lst[smallest], lst[x]



if __name__ == '__main__':

    # creating randomly fill list of numbers
    lst = [random.randint(1, 9) for _ in range(7)]
    print(f"Unsorted list: {lst}")

    # sorting the list, using the function we wrote
    selection_sort(lst)
    print(f"Sorted list: {lst}")
