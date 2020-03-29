import sys

def flatten(l):
    result = []
    for elem in l:
        if isinstance(elem, (list,tuple)):
            for e in flatten(elem): 
                result.append(e)
        else:
            result.append(elem)
    return result
    
print(flatten([[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]))