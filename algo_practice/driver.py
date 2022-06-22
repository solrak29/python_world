from selection import selection_sort
from selection_opt import selection_sort as sort_opt
from bubble_sort import bubble_sort

if __name__ == "__main__":
    value = [5,2,3,1,8,7]
    selection_sort(value)
    print(value)
    value = [5,2,3,1,8,7]
    sort_opt(value)
    print(value)
    value = [5,2,3,1,8,7]
    bubble_sort(value)
    print(value)

