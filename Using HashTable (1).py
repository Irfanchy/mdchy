__author__ = 'MD Irfan Chowdhury'
# Date 14/9/2016
import time
from task1 import HashTable


class HashTableV3(HashTable):
    # O(1) best, O(number of elements) worst
    def __setitem__(self, key, value):
        """
        Set the value in table and tie it with key.
        Raise KeyError if table is already full.

        :param immutable key:
        :param any value:
        """

        index = index_0 = self.hash(key)
        collisions = 0
        for i in range(1, self.table_size):
            if self.table[index] is None:
                # if position empty, just set item
                self.table[index] = [key, value, collisions]
                return
            elif self.table[index][0] == key:
                # if key in table, override
                self.table[index] = [key, value, collisions]
                return
            else:
                # resolve by probing
                index = self.probing(index_0, i)
                collisions = 1
        else:
            raise KeyError('Table is full.')

    # O(1) best, O(number of elements) worst
    def __getitem__(self, key):
        """
        Get value that corresponds to key.
        Raise KeyError if not found in table.

        :param immutable key: the key of value
        :return: tuple of (key, value, number of collisions)
        """

        index = index_0 = self.hash(key)
        for i in range(1, self.table_size):
            if self.table[index] is None:
                # if there is no element in position
                raise KeyError("No such key.")
            else:
                if self.table[index][0] != key:
                    # resolve collision by linear probing
                    index = self.probing(index_0, i)
                else:
                    return self.table[index]
        else:
            # if looked through whole table and still didn't found key
            raise KeyError("No such key.")


def test_time():
    size_list = [250727, 402221, 1000081]

    b_list = [1, 27183, 250726]

    filenames = ['english_small.txt', 'english_large.txt', 'french.txt']

    def read(filename, b, size):
        """
        Read file into hash table. Keys are read words, values are same as keys.
        Append time spent on reading to times dictionary.

        :param int size: size of hash table
        :param int b: parameter of hashing
        :param str filename: name of file
        """

        # print(filename, b, size)
        if size - b == 1:  # takes literally an eternity
            return float('inf'), 0

        table = HashTableV3(size)
        table.b = b
        collisions = 0
        start = time.time()
        with open(filename, 'r', encoding='utf8') as file:
            for word in file:
                word = word.strip()
                table[word] = word
                cols = table[word][2]
                if cols:
                    collisions += cols
        return time.time() - start, collisions

    for i in range(3):
        print(filenames[i] + ':')
        # for pretty output
        print('b\\size|{:13d}|{:13d}|{:13d}|'.format(*size_list))
        for j in range(3):
            times = [read(filenames[i], b_list[j], size_list[k]) for k in
                     range(3)]
            print('{0:6d}|{1[0]:6.3f}|{1[1]:6d}|{2[0]:6.3f}|{2[1]:6d}|'
                  '{3[0]:6.3f}|{3[1]:6d}|'.format(b_list[j], *times))

if __name__ == '__main__':
    test_time()

