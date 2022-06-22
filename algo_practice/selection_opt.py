
def selection_sort(a:[int] ):
    print(f'selection sort of {a}')
    for idx, val in enumerate(a):
        minIndex = idx
        for index in range(minIndex+1, len(a)):     
            if a[minIndex] > a[index]:
                minIndex = index
        tmp = a[idx] 
        a[idx] = a[minIndex]
        a[minIndex] = tmp
