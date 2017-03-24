__author__ = 'MD Irfan Chowdhury'
# Date 17/9/2016
from task4 import HashTableV4

TABLE_SIZE = 1000081


def create_freq_table(filename):
    """
    Perform analysis over book. Create table where for each word met in book
    string "common", "uncommon" or "rare" will correspond.
    Also count the ratio of common, uncommon and rare words in book.

    :param str filename: name of file with book
    :return: table, tuple(percent of common, of uncommon, of rare)
    """

    # reading book
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().lower().replace(',', ' ').replace('.', ' ').split()

    table = HashTableV4(TABLE_SIZE)
    # inserting words in table
    for word in words:
        try:
            table[word][1] += 1
        except KeyError:
            table[word] = 1

    # extract words and frequency for each word by iteration over table
    # (third element is number of collision upon setting and not needed here)
    dictionary = [pair[:2] for pair in table.table if pair is not None]

    # find most frequently occurred word
    max_occ = 0
    for pair in dictionary:
        if pair[1] > max_occ:
            max_occ = pair[1]

    freq_table = HashTableV4(TABLE_SIZE)
    common = uncommon = rare = 0.
    for pair in dictionary:
        #freq = input("Enter a word: ")
        freq = pair[1] / max_occ
        if freq > (1 / 100):
            freq_table[pair[0]] = 'common'
            common += freq
            print("The word you entered is common.")
        elif freq > (1 / 1000):
            freq_table[pair[0]] = 'uncommon'
            uncommon += freq
            print("The word you entered is uncommon.")
        else:
            freq_table[pair[0]] = 'rare'
            rare += freq
            print("The word you entered is rare.")
    return freq_table

if __name__ == '__main__':
    freq_table, frequencies = create_freq_table('book.txt')

    # normalize ratios to be percentage
    norm = 1 / sum(frequencies) * 100

    print("For ADVENTURES OF HUCKLEBERRY FINN results are:\n",
          frequencies[0] * norm, frequencies[1] * norm, frequencies[2] * norm)
