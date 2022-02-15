def binary_search(array, high, low, x):
    mid = (high + low) // 2  # Sets to the average of high and low (rounds down)

    if array[mid] == x:  # If the number in the middle of the array is equal to the desired number
        return mid  # Return that number (index)

    if high >= low:
        if array[mid] > x:  # If the number in the middle of the array is greater than the desired number
            return binary_search(array, mid-1, low, x)  # Call the recursive function with the shorted search array
        else:
            return binary_search(array, high, low+1, x)

    return -1  # If it gets through the array without finding the number, return -1



arr = [1, 2, 5, 7, 8, 9]
spot = binary_search(arr, len(arr)-1, 0, 10)

print(spot)
