
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

means = pd.read_csv("Averages100.csv",index_col=0)
# transpose the dataframe
means=means.T
plt.rcParams["figure.figsize"]=(16,8)
simpleSorts = means[['BubbleSort','InsertionSort']]
otherSorts=means[['MergeSort','QuickSort','CountingSort']]


means.plot(lw=2, colormap='jet', marker='.', markersize=10, 
title='Benchmarking Sorting Algorithms - Average Times')
plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")


#aplot =plt.rcParams["figure.figsize"]=(16,8)
#aplot.set(yscale="log")
f, axes = plt.subplots(2, 1, figsize=(12, 16))

simpleSorts.plot(lw=2, marker='.', markersize=10,ax=axes[0], colormap='jet')
otherSorts.plot(lw=2, colormap='Set1', marker='.', markersize=10,ax=axes[1])

plt.suptitle("Benchmarking Sorting Algorithms - Average Times")
plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")
#axes[0].legend()
#plt.legend()
plt.show()
"""
bubble.plot(lw=2, colormap='jet', marker='.', markersize=10, 
title='Benchmarking Sorting Algorithms - Average Times', ax=axes[0])
insertion.plot(ax=axes[0])

plt.ylabel("Running time (milliseconds)")
plt.xlabel("Input Size")
axes[0].set_title("Bubble Sort")
plt.show()
"""

# https://matplotlib.org/tutorials/colors/colormaps.html