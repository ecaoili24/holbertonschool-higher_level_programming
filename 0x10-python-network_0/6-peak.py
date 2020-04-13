#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Returns the peak in a list
    """
    if not list_of_integers:
        return None
    list_len = len(list_of_integers)

    return find_peak_recursive(list_of_integers, list_len)


def find_peak_recursive(arr, len_arr):
    """
    Finds the peak recursively
    """
    return recursion_peak(arr, 0, len_arr - 1, len_arr)


def recursion_peak(arr, low, high, len_arr):
    """
    Uses Binary Search that retunds the idx of peak elem in a list
    """
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len_arr - 1 or
                                                    arr[mid + 1] <= arr[mid])):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return recursion_peak(arr, low, (mid - 1), len_arr)

    else:
        return recursion_peak(arr, high, (mid + 1), len_arr)
