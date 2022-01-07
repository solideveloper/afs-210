import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:  #base case
        return

    # Call the partition helper function to split the list into two sections
    # divided between a pivot point
    # pivot = partitionStart(a_list, start, end)
    # pivot = partitionSecond(a_list, start, end)
    # pivot = partitionMiddle(a_list, start, end)
    pivot = partitionSecondLast(a_list, start, end)
    # pivot = partitionEnd(a_list, start, end)
    # pivot = partitionRandom(a_list, start, end)
    
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):   #first element
    #select the first value on list
    return partition(a_list, start, end)
#execution time is: 0.001455068588256836
#execution time is: 0.0015239715576171875
#execution time is: 0.0010809898376464844

def partitionSecond(a_list, start, end):
    #swap first and second elements on list
    #call partitin function which uses first element as pivot
    a_list[start], a_list[start+1] = a_list[start+1], a_list[start]
    return partition(a_list, start, end)
#execution time is: 0.014518022537231445
#execution time is: 0.016628265380859375
#execution time is: 0.014369010925292969

def partitionMiddle(a_list, start, end):
    mid = len(a_list) // 2
    a_list[start], a_list[mid] = a_list[mid], a_list[start]
    return partition(a_list, start, end)
#execution time is: 0.016835927963256836
#execution time is: 0.016835927963256836
#execution time is: 0.014004945755004883

def partitionSecondLast(a_list, start, end):
    a_list[end], a_list[end-1] = a_list[end-1], a_list[end]
    return partition(a_list, start, end)
#execution time is: 0.0014090538024902344
#execution time is: 0.0014369487762451172
#execution time is: 0.0014350414276123047

def partitionEnd(a_list, start, end):
    a_list[start] , a_list[end] = a_list[end], a_list[start]
    return partition(a_list, start, end)
#execution time is: 0.0012021064758300781
#execution time is: 0.0011188983917236328
#execution time is: 0.0012578964233398438

def partitionRandom(a_list, start, end):
    randomPivot = random.randrange(start, end)
    a_list[start] , a_list[randomPivot] = a_list[randomPivot], a_list[start]
    return partition(a_list, start, end)
#execution time is: 0.001153707504272461
#execution time is: 0.0011019706726074219
#execution time is: 0.0010900497436523438

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

# print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList)

print(f"The execution time is: {end_time-start_time}")


