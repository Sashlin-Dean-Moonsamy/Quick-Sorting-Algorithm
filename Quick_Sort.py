# Define quick sort function
def quick_sort(array):

    # Create variable for length
    length = len(array)

    # If there is only one value or less return the array
    if length <= 1:
        return array

    # Else set pivot to last value in list
    else:
        pivot = array.pop()

    # Create lists to for values smaller and greater than the pivot
    values_smaller = []
    values_bigger = []

    # Create for loop to assign values to correct list
    for value in array:
        if value > pivot:
            values_bigger.append(value)

        else:
            values_smaller.append(value)

    # Recursively return sorted list
    return quick_sort(values_smaller) + [pivot] + quick_sort(values_bigger)
