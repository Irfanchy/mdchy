__author__ = 'MD Irfan Chowdhury'
# Date 18/9/2016
from task6 import create_freq_table

table, frequencies = create_freq_table('book.txt')
with open('book2.txt', 'r') as file:
    words = file.read().lower().replace(',', ' ').replace('.', ' ')\
        .replace(':', ' ').replace(';', ' ').replace('"', ' ').split()
#words = input("Enter a word: ")
common = uncommon = rare = misspelled = 0.
for word in words:
    try:
        if table[word][1] == 'common':
            common += 1
            print("The word you entered is common.")
        elif table[word][1] == 'uncommon':
            uncommon += 1
            print("The word you entered is uncommon.")
        elif table[word][1] == 'rare':
            rare += 1
            print("The word you entered is rare.")
    except KeyError:
        misspelled += 1
        print("The word you entered is misspelled.")

# normalize ratios to be percentage
norm = 1 / (common + uncommon + rare + misspelled) * 100

print("For ADVENTURES OF TOM SAWYER results are:\n",
      common * norm, uncommon * norm, rare * norm, misspelled * norm)
