
def bubble_sort(a:[int]):
    print(f'Bubble Sort of {a}')
    a_len = len(a)
    for idx in range( a_len - 1, -1, -1 ):
        for iidx in range( idx - 1, -1, -1 ):
            if a[idx] < a[iidx]:
               tmp = a[idx]
               a[idx] = a[iidx]
               a[iidx] = tmp 
