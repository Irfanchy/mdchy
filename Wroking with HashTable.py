__author__ = 'MD Irfan Chowdhury'
# Date 11/9/2016
import time
from task1 import HashTable

size_list = [250727, 402221, 1000081]

b_list = [1, 27183, 250726]

filenames = ['english_small.txt', 'english_large.txt', 'french.txt']


def read(filename, b, size):
    """
    Read file into hash table. Keys are words that were read from file,
    values are same as keys.

    :param int size: size of hash table
    :param int b: parameter of hashing
    :param str filename: name of file
    """

    # works too long in this case
    if size - b == 1:  # takes literally an eternity
        return float('inf')

    table = HashTable(size)
    table.b = b
    start = time.time()
    with open(filename, 'r', encoding='utf8') as file:
        for word in file.readlines():
            table[word] = word
    return time.time() - start


for i in range(3):
    print(filenames[i] + ':')
    # for pretty output
    print('b\\size|{:13d}|{:13d}|{:13d}|'.format(*size_list))
    for j in range(3):
        times = [read(filenames[i], b_list[j], size_list[k]) for k in range(3)]
        print('{:6d}|{:13.3f}|{:13.3f}|{:13.3f}|'.format(b_list[j], *times))

