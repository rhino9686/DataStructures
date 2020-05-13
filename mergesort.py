

def mergesort(arr):
    start = 0
    end = len(arr) - 1
    mergesort_inner(arr, start, end)
    return arr



def mergesort_inner(arr, start, end):
    ## base case
    if (start >= end):
        return

    middle = (start + end)//2

    # all recursively on two halves
    mergesort_inner(arr, middle + 1, end)
    mergesort_inner(arr, start, middle)

    ## merge everything together

    temp = [0 for item in arr]
    temp_it = start

    first_half_it = start
    first_half_end = middle 

    second_half_it = middle + 1
    second_half_end = end

    ## merge the two halves back into a temp array
    while (first_half_it <= first_half_end and second_half_it <= second_half_end):
        if arr[first_half_it] < arr[second_half_it]:
            temp[temp_it] = arr[first_half_it]
            first_half_it += 1
        else:
            temp[temp_it] = arr[second_half_it]
            second_half_it += 1
        temp_it += 1

    ##copy remainders/ only one of the two will fire at ay given time
    while(first_half_it <= first_half_end):
        temp[temp_it] = arr[first_half_it]
        first_half_it += 1
        temp_it += 1

    while(second_half_it <= second_half_end):
        temp[temp_it] = arr[second_half_it]
        second_half_it += 1
        temp_it += 1

    ## copy everything back into array
    size = end - start + 1
    arr[start:(start + size) ] = temp[start:(start + size)]




def quicksort(arr):
    start = 0
    end = len(arr) - 1
    quicksort_inner(arr, start, end)

    return arr


def quicksort_inner(arr, left, right):
    ## Base case
    if left >= right:
        return

    #get a pivot point, in this case always use middle element
    pivot_i = (left + right)//2
    pivot = arr[pivot_i]

    ## partition array around pivot    
    index = partition(arr, left, right, pivot)
    
    ##recursively sort around index
    quicksort_inner(arr, left, index-1)
    quicksort_inner(arr, index, right)
    

def partition(arr, left, right, pivot):

    while (left <= right):
        while arr[left] < pivot:
            left +=1

        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left




























def main():
    
    arr = [3,6,4,8,4,1,3,5,3]

    arr2 = arr[:]

    sorted_arr = mergesort(arr)

    print(sorted_arr)

    sorted_arr = quicksort(arr2)
    print(sorted_arr)
if __name__ == "__main__":
    main()