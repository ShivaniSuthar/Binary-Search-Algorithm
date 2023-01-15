
def binary_search(target, arr, left, right):
    """
    ''' This function computes a binary search
    by taking in 4 parameters -
    target, arr, left, right where target is
    an element you are looking for, arr is the
    original list of numbes, left is the left 
    index of the list you search through, and 
    right is the right index of the list you 
    search through '''
    
    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 3
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [2, 3]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 12)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30], [8, 9, 10, 20, 30], [20, 30], [20]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 10)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [7, 8, 9, 10], [10], []]

    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 30
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [10, 40], [10], []]

    >>> arr = [1,8,5,3,8]
    >>> target = 5
    >>> binary_search(target, arr, 0, 4)
    [[1, 8, 5, 3]]

    >>> arr = [15, 3, 4, 5]
    >>> target = 15
    >>> binary_search(target, arr, 1, 3)
    [[3, 4], []]

    >>> arr = [32, 6, 0, 2]
    >>> target = 32
    >>> binary_search(target, arr, 0, 2)
    [[32, 6], []]

    """
    two = 2

    pos = int(((left+right)/two))
    empty = []

    if arr[pos] == target:
        empty.append(arr[left:right])
        return empty
    if right <= left:
        return [arr[left:right]] + empty
    elif arr[pos] > target:
        pos_2 = pos
        return [arr[left:right]] + empty + binary_search(target, arr, left, pos_2)
    else:
        pos_2 = pos + 1
        return [arr[left:right]] + binary_search(target, arr, pos_2, right)

