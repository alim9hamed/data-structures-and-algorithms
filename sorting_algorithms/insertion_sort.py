



def insertion_sort(array):
    # array = array.copy()
    for i in range(1,len(array)):
        j, value = i-1 , array[i]

        while j>= 0 and array[j] > value:
            array[j+1] = array[j]
            j -=1

        array[j+1] = value

    # return array


array = [14,556,8,41,2,90,-5,4,1,5,2]
# array = [1,2,3,4,5,6,22,8,9,10]
sorted_array = insertion_sort(array)
print(sorted_array)
# insertion_sort(array)

print("Array: ",array)