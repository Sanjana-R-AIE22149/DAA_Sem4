#BL.EN.U4AIE22149 - R. Sanjana
#Lab Assignment-1- part-3

#Question-1
def sum_pair(array,sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]+array[j]==sum and (array[i]!=array[j]):
                return (array[i],array[j])


#Question-2
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
        
def max_pdt(array):
    quick_sort(array,0,len(array)-1)
    max_pdt=array[-1]*array[-2]
    return max_pdt

#Question-3
def swap_sort(array):
    val1=None
    val2=None
    for i in range(len(array)-1):

        if array[i+1]<array[i]:
            if val1==None:
                val1=i
            else:
                val2=i+1
    temp=array[val1]
    array[val1]=array[val2]
    array[val2]=temp
    return(array)          

#Question-4
def binary_separate(array):
    counts=[0,0]
    for i in array:
        if i==0:
            counts[0]+=1
        else:
            counts[1]+=1
    string=counts[0]*'0'+counts[1]*'1'
    return list(string)
    
#Question-5
def inversion_count(array):
    n=len(array)
    count=0
    for i in range(n):
        for j in range(n):
            if (i<j) and (array[i]>array[j]):
                print(f"({array[i]},{array[j]})")
                count+=1
    print(f"Total count of inversions are: {count}")
    
#Question-6
def targetsum_n2(array,target):
    for i in array:
        for j in array:
            if i+j==target:
                print(f"Yes, {i}+{j}={target}")
                break

def targetsum_n2(array,target):
    quick_sort(array,0,len(array)-1)
    left=0
    right=len(array)-1
    while left<right:
        if array[left]+array[right]==target:
            return(array[right],array[left])
        elif array[left]+array[right]<target:
            left+=1
        else:
            right-=1
    return "No such pairs"
print(targetsum_n2([8,1,6,4],100))