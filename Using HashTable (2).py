__author__ = 'MD Irfan Chowdhury'
# Date 15/9/2016
import time
from task3 import HashTableV3


class HashTableV4(HashTableV3):
    # WARNING: there's no warrant that this method will resolve collision
    # even if table isn't fully filled
    # O(1) best and worst
    def probing(self, index, collision):
        """
        Quadratic probing for hash table.

        :param int collision: the number of collision
        :param int index:
        :return: new index
        """

        return (index + collision * collision) % self.table_size


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

        if size - b == 1:
            return float('inf'), 0

        table = HashTableV4(size)
        table.b = b
        collisions = 0
        start = time.time()
        with open(filename, 'r', encoding='utf8') as file:
            for word in file.readlines():
                table[word] = word
                collisions = collisions + table[word][2]
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
