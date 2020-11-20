def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    sums = {}

    for x in range(length):
        if weights[x] not in sums:
            sums[weights[x]] = x
        difference = limit - weights[x]
        if difference in sums:
            if x == sums[difference]:
                continue
            return sorted([sums[difference], x], reverse =True)

    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))

"""
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
"""