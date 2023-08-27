# Quick Sort using Hoare's partition scheme

#Time: O(N*LOG(N))
#Space: O(N)

def partition(a, start, end):

    pivot = a[start]
    i, j = start-1,end+1

    while True:

        while True:
            i += 1
            if a[i] >= pivot:
                break

        while True:
            j -= 1
            if a[j]<=pivot:
                break
        if i >= j:
            return j
        
        a[i], a[j] = a[j], a[i]

def quicksort(a, start, end):

    if start >= end:
        return
    
    pivot = partition(a, start, end)

    quicksort(a, start, pivot)
    quicksort(a, pivot+1, end)

if __name__ == "__main__":

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quicksort(a, 0, len(a)-1)
    print(a)
