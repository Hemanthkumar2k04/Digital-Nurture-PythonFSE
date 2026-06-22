def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0
        right_index = 0
        merged_index = 0

        while (left_index < len(left_half)) and (right_index < len(right_half)):

            if left_half[left_index] < right_half[right_index]:
                array[merged_index] = left_half[left_index]
                left_index += 1
            else:
                array[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_half):
            array[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1
        while right_index < len(right_half):
            array[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1


array = [32, 1, 34, 22, 90, 64]
print("Original array: ", array)
merge_sort(array)
print("Sorted array: ", array)
"""
O/P:
Original array:  [32, 1, 34, 22, 90, 64]
Sorted array:  [1, 22, 32, 34, 64, 90]
"""
