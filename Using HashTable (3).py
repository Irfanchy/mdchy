__author__ = 'MD Irfan Chowdhury'
# Date 15/9/2016
import time
from task1 import HashTable


class HashTableV5(HashTable):
    # O(1) best, O(number of elements) worst
    def __getitem__(self, key):
        """
        Get value that corresponds to key.
        Raise KeyError if not found in table.

        :param immutable key: the key of value
        :return: tuple (value, collisions)
        """

        index = self.hash(key)
        if self.table[index] is None:
            raise KeyError('No such key.')
        else:
            collisions = 0
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1], collisions
                else:
                    collisions += 1
            else:
                raise KeyError('No such key.')

    # O(1) best and worst (append is O(1))
    def __setitem__(self, key, value):
        """
        Set the value in table and tie it with key.
        Raise KeyError if table is already full.

        :param immutable key:
        :param any value:
        """

        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = [[key, value]]
        else:
            self.table[index].append([key, value])

    # O(table_size) best and worst
    def __contains__(self, req_key):
        """
        Check whether the requested key is in table.

        :param req_key: immutable
        :return: Boolean
        """

        index = self.hash(req_key)

        for pair in self.table[index]:
            if pair[0] == req_key:
                return True
        else:
            return False


def test_time():
    size_list = [250727, 402221, 1000081]

    b_list = [1, 27183, 250726]

    filenames = ['english_small.txt', 'english_large.txt', 'french.txt']

    def read(filename, b, size):
        """
        Read file into hash table. Keys are read words, values are same as keys.
        Append time spent on reading to times dictionary.

        :param str filename: name of file
        """

        if size - b == 1:
            return float('inf'), 0

        table = HashTableV5(size)
        table.b = b
        collisions = 0
        start = time.time()
        with open(filename, 'r', encoding='utf8') as file:
            for word in file.readlines():
                table[word] = word
                collisions = collisions + table[word][1]
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
