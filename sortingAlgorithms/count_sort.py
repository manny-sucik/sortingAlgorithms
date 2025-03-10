"""
================================================================================

  File Name: count_sort.py

  Purpose: Implementing count sort in Python.

  Creation Date: 10-03-2025

  Last Modified:

  Created By: Mansoud Mansouri

  Email: sucik@outlook.com

  Website: www.mansoud.com

=================================================================================
"""

def count_sort(lst):
    """
    A function to sort a given list of number using count sort algorithm.

    Algorithm:
    ----------
        >>> Find the min and max elements from the list 'lst'
        >>> Compute the range_size, the size of the temp list.
        >>> Create a count list 'count_lst' of length 'range_size', initialise it
            with 0s
        >>> For each value 'val' in 'lst', increment count_lst[val - min_element]
        >>> Reconstruct the original list 'lst' in sorted order

    Parameters:
    ----------
        lst: list()
            given unsorted list

    Returns:
    -------
        lst: list()
            given lst sorted
    """
    # if the list is empty or only has one element then no need for sorting the list
    if len(lst) < 2:
        return lst

    # find the min and max elements from the lst
    min_element = min(lst)
    max_element = max(lst)

    # compute the range_size
    range_size = max_element - min_element + 1

    # create and initialise the count_lst
    count_lst = [0] * range_size

    # count each element's occurrences
    for val in lst:
        count_lst[val - min_element] += 1

    # recreate the original list in sorted order
    index = 0
    for i, count in enumerate(count_lst):
        value = i + min_element
        while count > 0:
            lst[index] = value
            index += 1
            count -= 1
    return lst


if __name__ == "__main__":
    import random

    lst = [random.randint(1, 8) for _ in range(5)]
    print(f"Unsorted list: {lst}")

    count_sort(lst)
    print(f"sorted lst: {lst}")

    # lets create a list with some negative elements in it
    lst = [random.randint(-8, 5) for _ in range(5)]
    print(f"Unsorted list: {lst}")

    count_sort(lst)
    print(f"sorted lst: {lst}")
