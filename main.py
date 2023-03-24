def bubble_sort_while_loop(list):
    index_of_list = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for index in range(0, index_of_list):
            if list[index] > list[index + 1]:
                sorted = False
                list[index], list[index + 1] = list[index + 1], list[index]
    return list



def bubble_sort_for_loop(arr):
    n = len(arr)

    for i in range(n):
        print(n-i-1)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(arr):
    index_of_arr = range(1,len(arr))
    for i in index_of_arr:
        sort_value = arr[i]

        while arr[i-1] > sort_value and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

