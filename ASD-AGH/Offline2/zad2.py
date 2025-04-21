#Jakub Stachecki
#Program najpierw wybiera pierwsze p elementów, przekazuje je do tablicy pomocniczej i sortuje za pomocą merge sort. Następnie wybiera k-ty element oraz usuwa z tablicy pomocniczej pierwszy element z tablicy wejściowej.
# Następnie w pętli przechodzi przez całą tablicę podaną na wejściu i najpierw pobiera element z tablicy głównej, wstawia go w odpowiednie miejsce za pomocą funkcji find_spot_to_insert(tak,żeby tablica była cały czas posortowana
#i wybiera k-ty element. Nastepnie usuwany jest element ktory byl naszym elementem startowym(w petli jest to T[i]), za pomoca funkcji find_spot_to_remove.
#Złożoność czasowa programu to O(nlogp), gdzie n to dlugosc tablicy podanej na wejsciu, a pamięciowa to O(p)
from zad2testy import runtests


def find_spot_to_insert(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def find_spot_to_remove(array, x):
    left = 0
    right = len(array)
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < x:
            left = mid + 1
        elif array[mid] > x:
            right = mid - 1
        else:
            return mid


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


def ksum(T, k, p):
    workingArray = [0] * p
    element = T[0]

    for i in range(0, p):
        workingArray[i] = T[i]

    merge_sort(workingArray, 0, len(workingArray) - 1)
    sum = workingArray[p - k]
    workingArray.remove(element)

    for i in range(1, len(T) - p + 1):
        start = T[i]
        new = T[i + p - 1]
        workingArray.insert(find_spot_to_insert(workingArray, new), new)
        sum += workingArray[p - k]
        workingArray.pop(find_spot_to_remove(workingArray, start))
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
