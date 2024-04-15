#R. Sanjana - BL.EN.U4AIE22149
#Lab Sheet-4 - Design and Analysis of Algorithms
def fractional_knapsack(items,capacity):
    for i in items:
        i.append(i[1]/i[2])
        
    items.sort(key=lambda x:x[3],reverse=True)
    benefit=0
    knapsack=[]
    
    for i in items:
        if i[2]<=capacity:
            benefit+=i[1]
            knapsack.append((i[0],i[2]))
            capacity-=i[3]
        else:
            fraction=capacity/i[3]
            knapsack.append((i[0],fraction*i[1]))
            benefit+=fraction*i[1]
            break
        
    return benefit, knapsack

items = [['1',60,10],['2',100,20],['3',120,30]]
capacity = 50
#To run the first question uncomment the below line
# print(fractional_knapsack(items,capacity))

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
        
        
def max_sumarr(arr):
    quick_sort(arr,0,len(arr)-1)
    max_sum=0
    for i in range(len(arr)):
        max_sum=max_sum+(i*arr[i])
    return max_sum
arr=[2,5,3,4,0]
#Uncomment the below line to run the second question
#print(max_sumarr(arr))

arr1=[7,5,1,4]
arr2=[6,17,9,3]
def min_productsum(arr1,arr2):
    quick_sort(arr1,0,len(arr1)-1)
    arr2.sort(reverse=True)
    min_sum=0
    for i in range(len(arr1)):
        min_sum+=arr1[i]*arr2[i]
    print(min_sum)
#Uncomment the below line to run the third question.
# min_productsum(arr1,arr2)