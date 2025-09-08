"""
Linear Search Algorithm
-----------------------
Time Complexity:
    - Best Case: O(1)
    - Worst Case: O(n)
Space Complexity: O(1)

Description:
    Linear Search is the simplest searching algorithm.
    It sequentially checks each element of the list until
    the target element is found or the list ends.
"""

def linear_search(arr, target):
    """
    Performs linear search on the given list.

    Parameters:
        arr (list): The list of elements.
        target (any): The element to search for.

    Returns:
        int: The index of the target element if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    # Example usage
    data = [10, 20, 30, 40, 50]
    target = 30
    result = linear_search(data, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
