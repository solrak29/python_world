
def selection_sort(a:[int] ):
    print(f'selection sort of {a}')
    for idx, val in enumerate(a):
        minVal = a[idx]
        minIndex = idx
        for index in range(minIndex+1, len(a)):     
            if minVal > a[index]:
                minVal = a[index]
                minIndex = index
        tmp = a[idx] 
        a[idx] = minVal
        a[minIndex] = tmp
