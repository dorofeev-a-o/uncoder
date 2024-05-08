from bisect import bisect_left

n = [817, 1370, 752, 1247, 681, 1120, 915, 1281, 875, 1341, 757, 610, 812, 1170, 769, 1261, 845, 1289, 515, 1247, 845, 1311, 741, 1239, 812, 638, 877, 1242, 1159, 1372]
prices = [i for i in range(len(n))]
fruit_dictionary = dict(zip(prices, n))

print(fruit_dictionary)

myNumber = sum(n)/len(n)
list_sorted = n.sort()
def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

print("Среднее значение:", myNumber)
print("Медианное значение:", take_closest(list_sorted, myNumber))
print("Минимальное значение:", min(n))
print("Максимальное значение:", max(n))
