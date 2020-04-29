import random
import time
import pandas as pd
import numpy as np
import bubble
import merge
import counting
import insertion
import quick
   

def benchmarking(algorithms, Sizes, runs):
    # for each of the 5 sorting algorithms
    for algo in sort_type:
        print(f"running {algo}")
        #type.append(algo)
        # for each array size in the size array
        for size in Sizes:
            # run this 10 times for each size for each sort type
            for run in range(runs):
                # generate random arrays
                x = [random.randint(0,50) for i in range(size)]
                
                print(f" function {algo} on array of length {len(x)}")
                algorithm = sort_type[algo]
                #print(f"running {algo}")
                start_time = time.time()
                # run the actual algorithm on the current run on the current array size
                algorithm(x)
                end_time = time.time()
                time_elapsed = end_time - start_time
                
                # Here I want the results from each run, for each algo for each size
                # append the results of each run to the results array
                elapsed_times.append(time_elapsed)
                
                # append the current run number (from 1 to 10)
                trials.append(run+1)
                size_array.append(size)
                type.append(algo) # for each algorithm type 

                   
    df = pd.DataFrame({"Sort":type, "array sizes":size_array, "trial_time":elapsed_times, "trial number":trials})
    return df


if __name__ == "__main__":
    sort_type = {"BubbleSort": bubble.bubbleSort, "CountingSort": counting.CountingSort, "insertionSort":insertion.insertionSort, "mergeSort":merge.merge_sort, "quickSort":quick.quickSort}

    #sizeN = [100,250,500,750,1000,1250,2500,3750,5000,6250,7500,8750,10000]
    sizeN = [250,1000,2500,5000]


    print("running benchmarking")
    elapsed_times = [] # this should end up with 10 elapsed times 
    size_array =[]
    trials =[]
    averages = []
    size_array2=[]
    # for the averages dataframe
    sort_function =[]
    # for the averages dataframe 
    type =[]
    mydf = benchmarking(sort_type, sizeN, 10)

print("printing the resulting dataframe with the times")   
print(mydf)

mydf.to_csv('trial_times.csv')
averages = mydf.groupby(['Sort','array sizes']).mean()
averages.to_csv('average_times.csv')

x = averages.unstack()
x.to_csv("averages.csv")










    


    

    
