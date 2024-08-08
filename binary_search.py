numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(haystack, needle):
    """
    1. We first define low and high points, those help define the mid point.
    2. If the midpoint is the value, we return.
    3. When the guess > value, set the high to the mid we checked minus one.
    4. When the guess < value, set the low to the mid plus one.

    With an array of 128 values, this would take log 2 128 = 7
    With an array of 256 values, this would take log 2 256 = 8

    Binary search is O(log n) a.k.a log time complexity.
    """
    low = 0
    high = len(haystack) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = haystack[mid]
        if guess == needle:
            return mid
        elif guess > needle:
            high = mid - 1
        else:
            low = mid + 1
    return None


"""
Say you have 10 seconds, a.k.a 10,000ms
You need to search 1,000,000,000 items in an array.
Say binary search for 100 items is ~7ms.
Simple search for 100 items is ~1ms.

Binary search would take how many ms?
  1,000,000,000
  500,000,000
  250,000,000
  125,000,000
  62,500,000
  31,250,000
  15,625,000
  7,812,500
  3,906,250
  1,953,125
  ... ~ 30ms
Simple search would take how many ms?
  1,000,000,000ms ~ 11 days
"""

print(binary_search(numbers, 9))
