# def merge(left, right):
#     results = [None] * (len(left) + len(right))
#     i= j= k = 0

#     while i < len(left) and j < len(right):

#         if left[i] <= right[j]:
#             results[k] =  left[i]
#             i += 1
#         else:
#             results[k] =  right[j]
#             j += 1
#         k +=1

#     while i < len(left):
#         results[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         results[k] = right[j]
#         j += 1 
#         k += 1
#     return results


def merge(left, right):
    results = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    while i < len(left):
        results.append(left[i])
        i += 1

    while j < len(right):
        results.append(right[j])
        j += 1

    return results

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) //2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)





array = [14,556,8,41,2,90,-5,4,1,5,2]
# array = [1,2,3,4,5,6,22,8,9,10]
sorted_array = merge_sort(array)
# print(sorted_array)
# insertion_sort(array)

print("Array:",array)