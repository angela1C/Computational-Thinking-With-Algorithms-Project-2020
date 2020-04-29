"""
Code for the Bubble Sort algorithm. 
See [The BubbleSort](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
bubbleSort(alist)

"""

def bubbleSort(array):
    # The outer loop goes through the elements n-1 times, if n is the number of elements in the list

    for passnum in range(len(array)-1,0,-1):
        # count down to 0 as each time another element at the end of the list is sorted.
        # at each pass the last i elements are already in place so the inner loop is shorted by 1 each time
        for i in range(passnum): 
            # comparing each element i with the element right beside it (i+1)  
            if array[i] > array[i+1] : 
                # If the elements are out of order swap them so the largest element is right of the smaller one
                array[i], array[i+1] = array[i+1], array[i]


# optimised short bubble from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        print(f" in iteration {passnum} of the outer loop, {alist}")
        exchanges = False
        for i in range(passnum):
            print(f" In iteration {i} of the inner loop")
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

