def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    data = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    print("Array:", data)
    print("Linear Search for", target, "-> index:", linear_search(data, target))
    print("Binary Search for", target, "-> index:", binary_search(data, target))
    print("Recursive Binary Search for", target, "-> index:",
          binary_search_recursive(data, target, 0, len(data) - 1))
