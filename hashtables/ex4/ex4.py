def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # cache = {1:2}
    result = []

    for num in a:
        if num > 0:
            if num in cache:
                cache[num] +=1
            else:
                cache[num] = 1
            continue

        if abs(num) in cache:
            cache[abs(num)] += 1
        else:
            cache[abs(num)] = 1

    for key in cache:
        if cache[key] == 2:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

"""
..
----------------------------------------------------------------------
Ran 2 tests in 1.230s

OK
"""