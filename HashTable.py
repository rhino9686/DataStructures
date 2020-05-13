# sample python file
from enum import Enum

class Status(Enum):
    EMPTY = 1
    FILLED = 2
    GHOST = 3

class Bucket:
    def __init__(self):
        self.status = Status.EMPTY
        self.key = 0
        self.val = 0


class HashTable:

    """ Stores things according to a key/value system, with a linear probing mechanism for collision """

    """ Should have near O(1) insertion and lookup times with the constant resizing algorithm """

    ## Default constructor has an initial size of 20
    def __init__(self):
        ## array of buckets to store all items
        self.values = [ Bucket() for i in range(20)]

        ##keep running count of total live elements
        self.num_elements = 0

        ##also keep running count of total ghosts
        self.num_ghosts = 0

    
    def __getitem__(self,key):
        ##get hash of key for indexing
        index = hash(key) 
        initial_bucket = index % len(self.values)

        while(True):

            target = self.values[initial_bucket] 
            ## if we find the spot it's supposed to be in, get that value
            if (target.status == Status.FILLED and target.key == key):
                return target.val
            ## Once we've found the first empty slot, it means there is no item for that key
            if target.status == Status.EMPTY:
                return None

            initial_bucket = (initial_bucket + 1) % len(self.values)
        
        
    def __setitem__(self, key, value):
        ##get hash of key for indexing
        index = hash(key) 

        initial_bucket = index % len(self.values)

        while(True):
            target = self.values[initial_bucket] 
            ## if we find the spot it's supposed to be in, just update it
            if (target.status == Status.FILLED and target.key == key):
                self.values[initial_bucket].val = value
                return
            if target.status == Status.EMPTY:
                self.insert(key, value)
                return

            initial_bucket = (initial_bucket + 1) % len(self.values)
        return 


    def insert(self, key, item):

        self.recalculate_size()
        ##get hash of key for indexing
        index = hash(key) 
        initial_bucket = index % len(self.values)

        ghost_spotted = False
        ghost_index = -1

        while(True):
            target = self.values[initial_bucket] 
            ## if we find the spot it's supposed to be in, just update it
            if (target.status == Status.FILLED and target.key == key):
                return 
            ## find the first ghost and save the info for when you find an empty spot
            if target.status == Status.GHOST and not ghost_spotted:
                ghost_index = initial_bucket
                ghost_spotted = True

            ## find the first empty spot, put val in that or in first ghost
            if target.status == Status.EMPTY:
                if ghost_spotted:
                    initial_bucket = ghost_index
                    self.num_ghosts -= 1
                
                self.values[initial_bucket].status = Status.FILLED
                self.values[initial_bucket].key = key
                self.values[initial_bucket].val = item
                self.num_elements += 1
                return

            initial_bucket = (initial_bucket + 1) % len(self.values)


    def remove(self, key):
        ##get hash of key for indexing
        index = hash(key) 
        initial_bucket = index % len(self.values)

        while(True):
            target = self.values[initial_bucket] 
            ## if we find the spot it's supposed to be in, remove it and set as ghost
            if (target.status == Status.FILLED and target.key == key):
                target.status = Status.GHOST
                target.key = None
                target.val = None
                self.num_ghosts += 1
                self.num_elements += 1

            ## find the first empty spot, put val in that or in first ghost
            if target.status == Status.EMPTY:
                self.recalculate_size()
                return 


            initial_bucket = (initial_bucket + 1) % len(self.values)


    def recalculate_size(self):
        if( (self.num_elements + self.num_ghosts )/ len(self.values) > 0.5):
            self.re_hash_re_size()

    def re_hash_re_size(self):

        #copy all values into new array
        temp = self.values[:]
        newsize = len(temp) * 2

        #reset the sizes
        self.num_elements = 0
       
        
        self.values = [Bucket() for _ in range(newsize)]

        for bucket in temp:
            if bucket.status == Status.FILLED:
                self.insert(bucket.key, bucket.val)

        self.num_ghosts = 0

    def print_vals(self):
        for bucket in self.values:
            print("Bucket, key = {}, val = {}".format(bucket.key, bucket.val) )


