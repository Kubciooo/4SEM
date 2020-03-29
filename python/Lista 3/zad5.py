
def powerset(s):
    power_set = [[]]
    for elem in s:
        power_set = power_set + list(map(lambda x: list(x)+[elem], power_set))
    return power_set
print(powerset([1,2,3,4,5]))