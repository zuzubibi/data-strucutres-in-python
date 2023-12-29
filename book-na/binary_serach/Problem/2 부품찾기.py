def binary_serach(array, target, start, end):
    if start > end:
        return "No"
    
    mid = (start+end)//2

    if array[mid] == target:
        return "Yes"
    elif array[mid] > target:
        return binary_serach(array, target, start, mid - 1)
    else:
        return binary_serach(array, target, mid+1, end)
    



n = 5
store = [8,3,7,9,2]

m = 3
customer = [5,7,9]

store.sort()
customer.sort()

for i in range(len(customer)):
    print(binary_serach(store, customer[i], 0, len(store)-1), end=" ")
