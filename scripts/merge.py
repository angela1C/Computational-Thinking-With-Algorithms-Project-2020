"""
Merge Sort Algorithm - an efficient comparison based sort
# Code from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html

"""
# Code adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
# with comments.

def merge_sort(array):
    # the base case is a list with 0 or 1 elements which is is already sorted.

    if len(array)>1:
        # find the middle of the list using integer division to find the split point
        mid = len(array)//2
        # divide the elements into two halves using the mid point
        # # The elements are copied into the temporary arrays left[] and right[]
        # left contains the elements from the first half of the list (up to the mid)
        left = array[:mid]
        # right contains the elements from the second half of the list, (from mid to the end)
        right = array[mid:]
        # recursively call the function on the first (left) half
        merge_sort(left)
        # recursively call the function on the second (right) half
        merge_sort(right)

        # once the function has been called on the left and right half, each half should be sorted
        # The following code does the merge part, merging the two smaller lists into a single sorted list 
        # i, j and k represents the index of the left array, right array and merged arrays respectively.
        i ,j, k = 0,0,0
        # The elements are placed back into the original list (array) by repeatedly taking the smallest item from the two sorted lists.

        # until the left and right arrays are empty.
        while i < len(left) and j < len(right):
            # compare the first/next element in left and right arrays, if the left element is smaller, place this element next in the sorted array
            if left[i] <= right[j]:
                array[k]=left[i]
                # increment the index of left (for the next comparison between left and right arrays)
                i += 1
            else:
                # otherwise if the smallest element is in the right array, assign this element to the next position in the merged array
                array[k]=right[j]
                # increment the index of the right array (for the next comparison between left and right arrays)
                j += 1
            # after assigning another element to the merged array, increment the index by 1
            k=k+1
        # no elements left in right array so check if any element left in the left array, if so move to merged array
        while i < len(left):
            array[k]=left[i]
            i += 1
            k += 1
        # no elements left in left array, so check if any elements left in the right array, if so move to merged array
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1
    return array


import random
array = [random.randint(0,15) for i in range(5)]


if __name__ == "__main__":
    merge_sort(array)





# same MergeSort code from https://www.geeksforgeeks.org/merge-sort/ with different variable names
# alternative code from real python at https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python
def merge(left, right):
    # If the first array is empty, then nothing needs to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right
     # If the second array is empty, then nothing needs to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
# Now go through both arrays until all the elements make it into the resultant array
    while len(result) < len(left) + len(right):
         # The elements need to be sorted to add them to the resultant array, so you need to decide whether to get
         # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

# If you reach the end of either array, then you can add the remaining elements from the other array to
# the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break
    
        if index_left == len(left):
            result += right[index_right:]
            break
 
    return result




