

def bubble_sort(array):
    flag = True
    for i in range(0,len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]> array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
        if flag == True:
            return
    
    return array


# array = [14,556,8,41,2,90,-5,4,1,5,2]
array = [1,2,3,4,5,6,22,8,9,10]
sorted_array = bubble_sort(array)
print(sorted_array)