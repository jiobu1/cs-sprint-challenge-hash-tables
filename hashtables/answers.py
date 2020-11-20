def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # $%$Start
    ht = {}
​
    for i in range(length):
        d = limit - weights[i]
​
        if d in ht:
            complement = ht[d]
            answer = (i, complement)
            return answer
​
        else:
            ht[weights[i]] = i
    # $%$End
    return None

​#############################################################################
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # $%$Start
    hashtable = {}
    route = [None] * length
​
    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        hashtable[tickets[i].source] = tickets[i].destination
​
    for j in range(length):
        if route[j - 1] is not None:
            route[j] = hashtable[route[j - 1]]
    # $%$End
    return route
​
#############################################################################
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # $%$Start
    h = {}
​
    for a in arrays:
        for e in a:
            if e in h:
                h[e] += 1
            else:
                h[e] = 1
​
    result = []
​
    array_count = len(arrays)
​
    for k in h:
        if h[k] == array_count:
            result.append(k)
    # $%$End
    return result
​
#############################################################################
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # $%$Start
    h = {}
​
    for i in a:
        if i >= 0:
            h[i] = True
​
    result = []
​
    for i in a:
        if i < 0 and -i in h:
            result.append(-i)
    # $%$End
    return result
​
#############################################################################
def get_filename(f):
    i = f.rfind("/")
​
    if i == -1:
        return f
​
    return f[(i+1):]
# $%$End
​
​
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # $%$Start
    # Build index
​
    index = {}
​
    for full_path in files:
        filename = get_filename(full_path)
​
        if filename not in index:
            index[filename] = []
​
        index[filename].append(full_path)
​
    # Run queries
    result = []
​
    for q in queries:
        if q in index:
            result += index[q]
    # $%$End
    return result