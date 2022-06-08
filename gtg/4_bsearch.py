def bsearch(data, x, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if x == data[mid]:
            return True
        elif x < data[mid]:
            return bsearch(data, x, low, mid-1)
        else:
            return bsearch (data, x, mid + 1, high)
            