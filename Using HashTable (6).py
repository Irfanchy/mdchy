__author__ = 'MD Irfan Chowdhury'
# Date 18/9/2016
from task3 import HashTableV3


class HashTableV8(HashTableV3):
    # O(1) best, O(table_size) worst
    def delete(self, key):
        """
        Delete value that corresponds to key.
        Raise KeyError if not found in table.

        :param immutable key: the key of value
        :return: None
        """

        # current index and basic index to not recalc hash every time
        index = index_0 = self.hash(key)
        for i in range(self.table_size):
            if self.table[index] is None:
                # if there is no element in position
                raise KeyError("No such key.")
            else:
                if self.table[index][0] != key:
                    # resolve collision by probing
                    index = self.probing(index_0, i)
                else:
                    j = i  # to not modify loop variable
                    # shift all previously resolved values
                    while self.table[index][0] is not None:
                        self.table[index] = self.table[self.probing(index_0, j)]
                        index = self.probing(index_0, j)
                        j += 1
                    return
        else:
            # if looked through whole table and still didn't found key
            raise KeyError("No such key.")

    # O(number of elements)
    def rehash(self, size):
        if size < 1:
            raise ValueError('Size should be positive integer.')

        new_table = HashTableV8(size)

        try:
            for pair in self.table:
                if pair is not None:
                    new_table[pair[0]] = pair[1]

            self.table_size = size
            self.table = new_table.table
        except KeyError:
            raise ValueError('Size passed is smaller than number '
                             'of elements in table.')
