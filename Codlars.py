#5 Sum it continuously
def add(lst):
    cumulative_sums = []
    running_total = 0
    for num in lst:
        running_total += num
        cumulative_sums.append(running_total)

    return cumulative_sums

#6 Double Every Other
def double_every_other(lst):
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i] *= 2
    return lst

#7 List Filtering
def filter_list(l):
    return [i for i in l if isinstance(i, int)]

#8 Thinkful - List and Loop Drills: Inverse Slicer
def inverse_slice(items, a, b):
    return items[:a] + items[b:]

#9 Santa's Naughty List
def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))

#10 Test's results
from statistics import mean

def test(r):
    dct = {'l': 0, 'a': 0, 'h': 0}
    for n in r: dct['lah'[(n > 6) + (n > 8)]] += 1
    return [round(mean(r), 3), dct] + ['They did well'] * (sum(dct.values()) == dct['h'])

#11 Slice the middle of a list backwards
def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]

#12 Parts of a list
def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        result.append((' '.join(arr[:i]), ' '.join(arr[i:])))
    return result

#13 ORing arrays
from itertools import zip_longest

def or_arrays(a1, a2, d=0):
    return [x | y for x, y in zip_longest(a1, a2, fillvalue=d)]

#14 Remove the minimum
def remove_smallest(numbers):
    if not numbers:
        return []
    min_val = min(numbers)
    for i in range(len(numbers)):
        if numbers[i] == min_val:
            return numbers[:i] + numbers[i + 1:]
















