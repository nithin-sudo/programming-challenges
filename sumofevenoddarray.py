# Return sum of second largest element from even position and second smallest element from odd position

# initialized an array
nums = [10,45,11,1,22,2,4]

index = 0
evens = list()
odds = list()

# seperating evens and odds into their respective arrays
for num in nums :
    if(index % 2 == 0):
        evens.append(num)
    else:
        odds.append(num)
    index = index + 1

# bubble sort
# used bubble sort to sort each array, easy sorting algorithm but it is not fast enough.

''' first for loop, iterates through the whole array once, inside loop actually takes care of
comparing each element with adjacent element and swaps accordingly.'''

for i in range(0,len(evens)- 1):
    for  j in range(0,len(evens)-i-1):
        if evens[j] > evens[j+1]:
            evens[j],evens[j+1] = evens[j+1],evens[j]

for i in range(0,len(odds)-1):
    for j in range(0,len(odds)-i-1):
        if odds[j] > odds[j+1]:
            odds[j],odds[j+1] = odds[j+1],odds[j]

sum_of_elements = evens[len(evens) - 2] + odds[1]

print("sum of second largest element from even position and second smallest element from odd position: ", sum_of_elements)