from operator import ge as greaterEqual, lt as lesser

def sublist(L, op, pivot):
    return list(filter(lambda num: op(num, pivot), L))

def qsort(L):
    if len(L) <= 1: return L
    pivot   = L[0]
    t = L[1:]
    return qsort(sublist(t, lesser, pivot)) + [pivot] + qsort(sublist(t, greaterEqual, pivot))
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(qsort(array))
