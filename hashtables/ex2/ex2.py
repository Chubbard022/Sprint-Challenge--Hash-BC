#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    home = "home"
    
    for i in tickets:
        if i.source is "NONE": 
            hash_table_insert(hashtable, home, i.destination)
        else:
            hash_table_insert(hashtable, i.source, i.destination)

    for i in range(0, len(route)):
        dest = hash_table_retrieve(hashtable, home)

        route[i] = dest
        home = dest

    return route
