def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None:  # If target is greater than any array element
        upper_bound = float("inf")  # Indicate no upper bound within the array

    return (iterations, upper_bound)


def main():
    # Example array and target
    arr = [0.5, 1.2, 3.8, 4.5, 5.9, 7.3]
    target = 4.5

    # Run the binary search
    iterations, upper_bound = binary_search_with_upper_bound(arr, target)
    print(f"Target: {target}")
    print(f"Upper bound: {upper_bound}")
    print(f"Iterations: {iterations}")


if __name__ == "__main__":
    main()
