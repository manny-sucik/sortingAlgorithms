"""
================================================================================

  File Name: insertion_sort.py

  Purpose: Implementing insertion sorting algorithm in Python.

  Creation Date: 06-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""
import random

def insertion_sort(lst):
    """
    A function to sort an unsorted list with insertion algorithm.

    Algorithm:
    ----------
            >>> Consider the first element in the list to be sorted
                (correctly placed)
            >>> Start from the second element, for each element(call it the key),
                compare it with the elements in the sorted part of the list.
            >>> If the key is smaller than an element in the sorted part, shift
                that element one position to the right. Continue shifting until
                you find the correct position for the key!
            >>> Place the key in its correct position.
            >>> Continue with the next element until the entire list is sorted!

    Parameters:
    -----------
        lst: list()
                list to be sorted

    Returns:
    --------
        lst: list()
                the sorted list.
    """
    # Iterate over the list starting from the second element
    for i in range(1, len(lst)):
        key = lst[i] # the first key will be the second element!
        j = i - 1

        # shift elements that are greater than the key to the right
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j-=1

        # insert the key at the correct position
        lst[j+1] = key

    return lst

# make a list of random numbers
lst = [random.randint(1, 8) for _ in range(5)]

print(f"Unsorted list: {lst}")

# using the above function to sort the list
insertion_sort(lst)
print(f"Sorted list: {lst}")
