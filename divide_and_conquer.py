import pudb

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


print(recursive_sum(numbers))


def recursive_count(numbers):
    if not numbers:
        return 0

    return 1 + recursive_count(numbers[1:])


print(recursive_count(numbers))


def recursive_maximum(numbers):
    if len(numbers) == 1:
        return numbers[0]

    max_of_rest = recursive_maximum(numbers[1:])

    if list[0] > max_of_rest:
        return list[0]
    else:
        max_of_rest


print(recursive_count(numbers))


def binary_search(numbers, to_find):
    if not numbers:
        return -1  # Target not found

    mid = len(numbers) // 2

    if numbers[mid] == to_find:
        return mid  # Target found at index mid
    elif numbers[mid] < to_find:
        # Search the right half
        result = binary_search(numbers[mid + 1 :], to_find)
        if result != -1:
            return mid + 1 + result  # Adjust index for the right half
    else:
        # Search the left half
        return binary_search(numbers[:mid], to_find)

    return -1


print(binary_search(numbers, 4))


def quicksort(numbers):
    if len(numbers) < 2:
        print(f"numbers: {numbers}")
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
        print(pivot)
        print(numbers)
        print(less)
        print(greater)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([4, 5, 2, 1, 6, 8, 9, 7]))
