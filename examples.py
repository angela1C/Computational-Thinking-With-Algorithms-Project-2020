# some examples here for illustration with some print statements

def bubbleSortP(array):

    
    print(f"The number of passes required will be {len(arr)-1} on a list of size {len(arr)}")

    for passnum in range(len(array)-1,0,-1): # goes through the process 49 times
        print(f" in iteration {passnum} of the outer loop, {array}")
        for i in range(passnum): 
            print(f" In iteration {i} of the inner loop")
            # comparing each element j with the element beside it (i+1) 
 
            if arr[i] > arr[i+1] : 
                print(f" A swap is required here for elements {arr[i],arr[i+1]}")
                # If the elements are out of order swap them so 
                arr[i], arr[i+1] = arr[i+1], arr[i]

import random
# a random array of 10 elements 

#myarray = [random.randint(0,15) for i in range(5)]
myarray = [6,11,3,9,4]
print(f"The array to be sorted {myarray}")
print(bubbleSortP(myarray))
print(f"The array after being sorted {myarray}")

# an example to show worst case

array = [5,4,3,2,1]
print(f"The array to be sorted {array}")
print(bubbleSortP(array))
print(f"The array after being sorted {array}")

# an example to show best case

array = [1,2,3,4,5]
print(f"The array to be sorted {array}")
print(bubbleSortP(array))
print(f"The array after being sorted {array}")

## my adapted code with comments.

def merge_sort(array):
    print("Splitting ",array)
    #if len(array) <=1:
        #print("array with 0 or 1 elements")
# the base case is if the list has 1 or zero elements, if so the rest of the code will not run as it is already sorted.

    if len(array)>1: # same as 'if len(array) < 2:'
        # find the middle of the list using integer division
        mid = len(array)//2
        # create two halves of the array using the mid as the dividing point, divide the elements into two halves
        # left contains the elements from the first half of the list, from the start of the array up to the mid point 
        left = array[:mid]
        # right contains the elements from the second half of the list, from the midpoint up to the end of the array 
        right = array[mid:]
        # recursively call the function on the first (left) half
        merge_sort(left)
        # recursively call the function on the second / right half
        merge_sort(right)

    # once the function has been called on the left and right half, each half should be sorted
    # The code below then does the merge part, merging the two smaller lists into a single sorted list

        # from here the code merges the two smaller 
        # enter a while loop
        # i represents the index of the left array, j the index for the right array and k the index for the merged array
        i ,j, k = 0,0,0

        # The elements are copied into the temporary arrays left[] and right[] by comparing the elements in the two halves
        # The elements are placed back into the original list (array) by repeatedly taking the smallest item from the two sorted lists.

        # until the left and right arrays are empty ??
        while i < len(left) and j < len(right):
            print(f" left array: {left} , right array {right}")
            #print(f" While i {i} is less than {len(left)} AND {j} is less than  {len(right)}")
            # compare the first/next element in left and right arrays, if the next element is less than the next element in right
            if left[i] <= right[j]:
                # assign that smallest element to the next position in the merged array
                array[k]=left[i]
                #print(f"Into merged goes {left[i]} and i becomes {i+1}")
                # increment the index of left (for the next comparison between left and right arrays)
                i=i+1
            else:
                # otherwise if the smallest element is in the right array, assign this element to the next position in the merged array
                array[k]=right[j]
                #print(f"into merged goes {right[j]} and j becomes {j+1}")
                # increment the index of the right array (for the next comparison between left and right arrays)
                j=j+1
            # after assigning another element to the merged array, increment the index by 1
            k=k+1
        # no elements left in right array so check if any element left in the left array, if so move to merged array
        while i < len(left):
            #print(f" Left: While i {i} is less {len(left)} ")
            array[k]=left[i]
            print(f" Into merged goes {left[i]}")
            i=i+1
            k=k+1
        # no elements left in left array, so check if any elements left in the right array, if so move to merged array
        while j < len(right):
            #print(f" Right: while j {j} is less than  {len(right)} ")
            array[k]=right[j]
            print(f" Into merged goes {right[j]}")
            j=j+1
            k=k+1
    print("Merging ",array)


# Counting sort for printing example output

def myCountingSortp(array):

    n= len(array)
    
    counter= [0 for i in range(max(array)+1)]
    # an array to store the sorted 
    sorted = []
    print (f"The length of the array to be sorted {array} is {len(array)}")
    print(f"The length of the counter array  {counter} is {len(counter)}")
    print(len(array))
    print(len(counter))

    for i in array:
        
       counter[i] += 1
    print(counter)

    for i in range(0,len(counter)):
        # while the counter shows that there is a matching element
        while counter[i] > 0:
            # append the element to the sorted array
            sorted.append(i)
           # decrease the counter by 1 each time
            counter[i] -= 1
    return sorted



###################################################################
# printing for example
def insertionSortP(array):
    # starting at the 2nd element in the list of item, at index 1
    for i in range(1,len(array)):
    # iterate through the array, each time setting the key to be the next element in the array
    # the key is the item to be positioned  
        key = array[i]
        print(f"key {key} is the element at a{[i]}")
        #print(f" array before next iteration {array}")
    # initialise j, j to be used to find the correct position of the key element, looks to element left of the current key
        j = i -1
    # while key element is smaller than elements to it's left, move all elements greater than the key right by one position
        while j >= 0 and array[j] > key:
            print(f" moving {array[j]} at a{[j]} to a{[j+1]}  ")
            array[j+1] = array[j]
            
         # reposition j to point to the next element
            j -= 1
            

    # after shifting elements, move key to its correct new position after the element just smaller than it.
        print(f" inserting {key} at a{[j+1]}")
        array[j+1]=key
        print(array)

#alist = [54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#print(alist)


### Quick Sort with some print statements for an example
def quickSortP(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       print(f"splitpoint: {splitpoint}")

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]
   print(f"pivot {pivotvalue}")

   leftmark = first+1
   rightmark = last
   print(f"leftmark {leftmark}, rightmark {rightmark}")
   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           print(f"leftmark {leftmark} <= rightmark {rightmark} AND leftmark {leftmark} <= pivot {pivotvalue}")
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           print(f"rightmark {rightmark} >= pivot {pivotvalue} AND rightmark {rightmark} >= leftmark {leftmark}")
           rightmark = rightmark -1

       if rightmark < leftmark:
           print(f" rightmark{rightmark} < leftmark {leftmark} so done.")
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark