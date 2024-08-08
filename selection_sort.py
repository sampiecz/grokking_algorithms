numbers = [5, 1, 10, 3, 4, 0, 6, 2, 8, 9, 7]


def findSmallest(numbers):
    """
    Helper function for selection sort. Finds the smallest number in an array.

    Set smallest to the first number of the array. Index is also kept track of.

    Then loop through the remainder of the passed in array.
    At each index, check if the current number is smaller than what we stored.
    If the current index is smaller, then update the smallest & index.

    Once all items are checked, return the smallest number.

    Runs in O(n) time since each item has to be checked.
    """
    smallest = numbers[0]
    smallest_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_index = i
    return smallest_index


def selectionSort(numbers):
    """
    SelectionSort sorts an array of numbers from low to high.
    It depends on the functionality within findSmallest.

    Define an empty array, and new list copy of the passed in array.
    Iterate over each item in the list copy.
    Check for the smallest number in the list copy.
    Then append the smallest number to our initially empty list.
    When storing new smallest number, pop the smallest number off list copy.

    SelectionSort is O(n^2) because we have two for loops.
    """

    sortedNumbers = []
    copiedNumbers = list(numbers)

    for _ in range(len(copiedNumbers)):
        smallest = findSmallest(copiedNumbers)
        sortedNumbers.append(copiedNumbers.pop(smallest))

    return sortedNumbers


print(selectionSort(numbers))
