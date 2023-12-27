def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    
    return arr

arr = [7,5,9,0,3,1,6,2,4,8]
# print(arr)
new_arr = selection_sort(arr)
print(new_arr)