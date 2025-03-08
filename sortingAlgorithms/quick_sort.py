"""
================================================================================

  File Name: quick_sort.py

  Purpose: Implementing quick sort algorithm in Python.

  Creation Date: 08-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""


def quick_sort(lst):
    """
    This function will sort a given list of number using quick sort algorithm.

    Algorithm:
    ---------
        >>> Choose a pivot from the list.
            This is an element from the list which you will compare and choose
            where to place othe elements from the list!

        >>> The partition the list into lists which contains the elements which
            are smaller and elements which are bigger than the pivot eleemnt.

        >>> Then recursively sort the sublists and then the recursion done, the
            list is sorted!

    Parameters:
    ----------
        lst: list()
             An unordered list which needs to be sorted.

    Returns:
    -------
        lst: list()
            The unsorted list sorted!
    """
    # this is the base case of the recursion.
    if len(lst) <= 1:
        return lst

    # picking the first element in the list as pivot here!
    pivot = lst[0]

    # a list containning all the smaller elements than pivot
    smls = [x for x in lst[1:] if x < pivot]

    # a list containning all the bigger elements than pivot
    bgs = [x for x in lst[1:] if x >= pivot]

    # now recursively call the function on itself and return the result!
    return quick_sort(smls) + [pivot] + quick_sort(bgs)


if __name__ == "__main__":
    import random

    # creating a list of random numbers
    lst = [random.randint(2, 9) for _ in range(5)]

    print(f"Unsorted list: {lst}")

    # sort the list using the function we wrote
    lst = quick_sort(lst)
    print(f"Sorted list: {lst}")

