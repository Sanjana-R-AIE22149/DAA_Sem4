#BL.EN.U4AIE22149 - R. Sanjana 
#DAA Lab Assignment 1 - Part 1

import matplotlib.pyplot as plt
import time
import random
#Question-1
def sum_iterative(n):
    #Iterative method
    start=time.time()
    sum_iterative=0
    for i in range(1,n+1):
        sum_iterative+=i
        
    end=time.time()
    return (end-start,sum_iterative)

def sum_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum_recursive(n-1)
    
def question1():
    
    n_string=input("Enter the values of n separated by space:")
    N=[int(x) for x in n_string.split()]
    times_i=[]
    times_r=[]
    for n in N:
        
        (time_iterative,sum_i)=sum_iterative(n)
    
        start=time.time()
        sum_r=sum_recursive(n)
        end=time.time()
    
        time_recursive=end-start
        times_i.append(time_iterative)
        times_r.append(time_recursive)
    print(times_i)
    print(times_r)
    plt.scatter(N,times_i,label="Iterative Method")
    plt.scatter(N,times_r,label="Recursive method")
    plt.xlabel('N')
    plt.ylabel("Time (in s)")
    plt.legend()
    plt.show()

def linear_search(array,ele):
    for i in range(0,len(array)):
        if array[i]==ele:
            return i
    return None

def binary_search(array,ele,start,end):
    mid=int((start+end)/2)
    if ele==array[mid]:
        return mid
    elif ele<array[mid]:
        return binary_search(array,ele,start,mid-1)
    else:
        return binary_search(array,ele,mid+1,end)
        
def question2():
    array=[random.randint(1,1000) for _ in range(10000)]
    array.sort()
    
    ele=(input("Enter the elements to search: "))
    elements=[int(x) for x in ele.split()]
    lin_start=time.time()
    for ele in elements:
        print(linear_search(array,ele))
    lin_end=time.time()
    
    bin_start=time.time()
    for ele in elements:
        print(binary_search(array,ele,0,len(array)-1))
    bin_end=time.time()
    
    print(f"Linear search time: {lin_end-lin_start}s")
    print(f"Binary search time: {bin_end-bin_start}s")
    
#Question-3
def recursive_digit(digit):
    if len(digit)==0:
        return 0
    
    remain=recursive_digit(digit[1:])
    d=int(digit[0])
    d=d*(10**(len(digit))-1)+remain
    return d


#Question-4
def recursive_reverse(string):
    if len(string)<=1:
        return (string)
    return recursive_reverse(string[1:])+string[0]
#Question-5
def recursive_palindrome(string):
    if len(string)<=1:
        return True
    
    if string[0]==string[-1]:
        return recursive_palindrome(string[1:-1])
    else:
        return False

print(recursive_palindrome("Sanjana"))