#BUBBLE SORT 
#compares the adjacent elements and swaps them if they are in the wrong order 
#Repeated until list is sorted
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                if not swapped:
                    break
list = [4,78,56,13,45,67,1,99]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                if not swapped:
                    break

bubble_sort(list)
print(list)
