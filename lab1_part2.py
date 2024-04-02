#BL.EN.U4AIE22149- R. Sanjana
#Lab Assignement-1 Part 2

import random
import time
import matplotlib.pyplot as plt
def insertion_sort(array):
    for i in range(1,len(array)):
        ele=array[i]
        j=i-1
        while j>=0 and ele<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=ele
    return array

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                
    return array

def selection_sort(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if array[min]>array[j]:
                min=j
        array[i],array[min]=array[min],array[i]
        
    return array
def partition(array,l,h):
    pivot=array[h]
    i=l-1
    for j in range(l,h):
        if array[j]<=pivot:
            i=i+1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
    temp2=array[i+1]
    array[i+1]=array[h]
    array[h]=temp2
    return i+1

def quick_sort(array,l,h):
    if l<h:
        pi=partition(array,l,h)
        quick_sort(array,l,pi-1)
        quick_sort(array,pi+1,h)
        

#Question-1
def question1():
    array=[]
    array=[random.randint(1,10000) for _ in range(1,1000)]
    times=[]
    start_select=time.time()
    print(f"Selection sort: {selection_sort(array)}")
    end_select=time.time()
    times.append(end_select-start_select)
    
    start_insert=time.time()
    print(f"Insertion sort: {insertion_sort(array)}")
    end_insert=time.time()
    times.append(end_insert-start_insert)
    
    start_bubble=time.time()
    print(f"Bubble sort: {bubble_sort(array)}")
    end_bubble=time.time()
    times.append(end_bubble-start_bubble)
    
    # start_quick=time.time()
    # print(f"Quick sort: {quick_sort(array,0,len(array)-1)}")
    # end_quick=time.time()
    # times.append(end_quick-start_quick)
    
    print(times)
    
#Question-2
def print_sorted(arrays):
    list_elements=[]
    for array in arrays:
        for i in array:
            list_elements.append(i)
    quick_sort(list_elements,0,len(list_elements)-1)
    print(list_elements)

#Question-3
def klargest(array,k):
    quick_sort(array,0,len(array)-1)
    values=[]
    for i in range(1,k+1):
        values.append(array[-1*i])
    print(array)
    print(values)
    
def max_activities(array):
    array.sort(key=lambda x: x[1])
    activities=[array[0]]
    count=0
    for i in range(len(array)):
        if activities[-1][1]<=array[i][0]:
            activities.append(array[i])
            count+=1
    print(activities)

def nonoverlapping_intervals(array):
    array.sort(key=lambda x:x[0])
    merged_intervals=[array[0]]
    for i in range(1,len(array)):
            if array[i][0]<=merged_intervals[-1][1]:
                merged_intervals[-1]=(merged_intervals[-1][0],max(merged_intervals[-1][1],array[i][1]))
                
            else:
                merged_intervals.append(array[i])
    print(merged_intervals)

