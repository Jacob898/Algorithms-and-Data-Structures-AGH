def merge_sort(array, left, right):
    def merge(array, left, mid, right):
        len1 = mid - left + 1
        len2 = right - mid

        array1 = array[left:mid + 1]
        array2 = array[mid + 1:right + 1]

        index1 = index2 = 0
        main_index = left

        while index1 < len1 and index2 < len2:
            if array1[index1] <= array2[index2]:
                array[main_index] = array1[index1]
                index1 += 1
            else:
                array[main_index] = array2[index2]
                index2 += 1
            main_index += 1

        while index1 < len1:
            array[main_index] = array1[index1]
            index1 += 1
            main_index += 1
        while index2 < len2:
            array[main_index] = array2[index2]
            index2 += 1
            main_index += 1

    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

