"""
================================================================================

  File Name: merge_sort.py

  Purpose: Implementing merge sort in Python.

  Creation Date: 08-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""

def merge(left_lst, right_lst):
    """
    This function will merge the two sorted lists into one sorted list.

    Algorithm:
    ---------
        >>> Start with two indices, one for each sorted given lists.
        >>> We need a list to hold the merged list, this will hold the sorted
            elements as you merged the lists.
        >>> While neighter indices has reached the end of its list, compare the
            elements, and append the appropriate one to the sorted list.
        >>> After the while loop, one fo the list might still have elements left_lst
            add the elements to the sorted list.
        >>> Return the merged list

    Parameters:
    ----------
        left_lst: list()
            The first sorted list.
        right_lst: list()
            The other sorted list.

    Returns:
    -------
        lst: list()
            The two given lists merged into one list.
    """

    merged_lst = list() # the list to hold the merged lists
    i, j = 0, 0 # indices to loop over the lists!

    # loop over the list while there are elements in both
    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] <= right_lst[j]:
            merged_lst.append(left_lst[i])
            i += 1
        else:
            merged_lst.append(right_lst[j])
            j += 1

    # if there is any element left in the left_lst, add them
    while i < len(left_lst):
        merged_lst.append(left_lst[i])
        i += 1

    # if there is any element left in the right_lst, add them
    while j < len(right_lst):
        merged_lst.append(right_lst[j])
        j += 1

    return merged_lst

def merge_sort(lst):
    """
    This function uses the merge algorithm to sort a list!

    Merge sort uses the merge algorithm as its key operation to sort
    a list.

    Algorithm:
    ---------
        >>> Split the list into two halves
        >>> Recursively sort each half
        >>> Use the merge algorithm to combine the two sorted halves

    Parameters:
    -----------
        lst: list()
            The list which needs to be sorted.

    Returns:
    --------
        lst: list()
            The list sorted.
    """
    # the vase case of the function!
    # because a list with just one element in SORTED!
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])

    # merge the lists and return
    return merge(left_lst, right_lst)

if __name__ == "__main__":
    import random

    # creating a list of random numbers
    lst = [random.randint(1, 12) for _ in range(8)]
    print(f"Unsorted list: {lst}")

    lst = merge_sort(lst)
    print(f"Sorted list: {lst}")
