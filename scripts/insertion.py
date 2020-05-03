"""
Benchmarking Sorting Algorithms Project
Angela Carpenter

Insertion Sort algorithm

Code adapted and commented based on java code in Computational Thinking with Algorithms lecture notes and python code at  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
and geekforgeeks.com
"""


# my adapted and commented version based on lecture notes and codes at interactive python, geeks etc.
def InsertionSort(array):
    # starting at the 2nd element in the list of item, at index 1
    for i in range(1,len(array)):
    # iterate through the array, each time setting the key to be the next element in the array
    # the key is the item to be positioned  
        key = array[i]
    # initialise j, j to be used to find the correct position of the key element, looks to element eft of the current key
        j = i -1
    # while key element is smaller than elements to it's left, move all elements greater than the key right by one position
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
         # reposition j to point to the next element
            j -= 1

    # after shifting elements, move key to its correct new position after the element just smaller than it.
        array[j+1]=key



    
