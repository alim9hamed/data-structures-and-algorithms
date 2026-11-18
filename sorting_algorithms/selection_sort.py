def selection_sort(array):
    
    for i in range(0, len(array)-1):
        min_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

array = [14,556,8,41,2,90,-5,4,1,5,2]

sorted_array = selection_sort(array)
print(sorted_array)
