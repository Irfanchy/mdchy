__author__ = 'MD Irfan Chowdhury'
# Date 10/9/2016
class HashTable:
    def __init__(self, size):
        """
        Create hash table object.

        :param int size: number of elements in hash table.
        """

        self.table_size = size
        # None instead of key value pair will indicate empty place
        self.table = [None for _ in range(size)]

        # parameter for hash function. we will need to play with this later
        self.b = 27183
        
    # O(len(key)) best and worse
    def hash(self, key):
        """
        Compute the hash value of key.

        Uses universal method with fast implementation for integers and
        positional depending implementation for string and floats.

        :param any key: key to be hashed
        :return: hash of key
        """

        if type(key) == int:
            return key % self.table_size
        else:
            # basically any object that has __str__ defined can serve as key
            key = str(key)

        value = 0
        a = 31415
        for i in range(len(key)):
            value = (a * value + ord(key[i])) % self.table_size
            a = a * self.b % (self.table_size - 1)

        return value

    # this is implemented as separate method to allow its latter overriding
    # with quadratic or double hash or w/e other probing
    # O(1) best and worse
    def probing(self, index, collision):
        """
        Linear probing for hash table.

        :param int collision: number of collision
        :param int index: base index
        :return: new index
        """

        return (index + collision) % self.table_size

    # O(1) best, O(number of elements) worst
    def __getitem__(self, key):
        """
        Get value that corresponds to key.
        Raise KeyError if not found in table.

        :param immutable key: the key of value
        :return: item
        """

        # current index and basic index to not recalc hash every time
        index = index_0 = self.hash(key)
        for i in range(1, self.table_size):
            if self.table[index] is None:
                # if there is no element in position
                raise KeyError("No such key.")
            else:
                if self.table[index][0] != key:
                    # resolve collision by probing
                    index = self.probing(index_0, i)
                else:
                    return self.table[index][1]
        else:
            # if looked through whole table and still didn't found key
            raise KeyError("No such key.")

    # O(1) best, O(number of elements) worst
    def __setitem__(self, key, value):
        """
        Set the value in table and tie it with key.
        Raise KeyError if table is already full.

        :param immutable key:
        :param any value:
        """

        # current index and basic index to not recalc hash every time
        index = index_0 = self.hash(key)
        for i in range(1, self.table_size):
            if self.table[index] is None:
                # if position empty, just set item
                self.table[index] = [key, value]
                return
            elif self.table[index][0] == key:
                # if key in table, override
                self.table[index] = [key, value]
                return
            else:
                # resolve by linear probing
                index = self.probing(index_0, i)
        else:
            raise KeyError('Table is full.')

    # O(table_size) best and worst
    def __contains__(self, key):
        """
        Check whether the requested key is in table.

        :param immutable key:
        :return: Boolean
        """

        for element in self.table:
            if element is not None:
                if element[0] == key:
                    return True
        else:
            return False