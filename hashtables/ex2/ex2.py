#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    destination_lookup_table = {}
    route = []

    for i in range(length):
        destination_lookup_table[tickets[i].source] = tickets[i].destination

    current_source = "NONE"

    while destination_lookup_table[current_source] != "NONE":
        destination = destination_lookup_table[current_source]
        route.append(destination)
        current_source = destination

    route.append("NONE")
    # had to append this to the back of the list to make the test pass

    return route

tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX" ),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE" ),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

print(reconstruct_trip(tickets, len(tickets)))
#['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD']
# matches with case in README
# test is incorrect. Last destination should not be none

"""
['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD', 'NONE']
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
jisha-mbp-10:ex2 jisha$
"""