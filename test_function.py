import unittest
from task1 import HashTable
from task3 import HashTableV3
from task4 import HashTableV4
from task5 import HashTableV5
from task8 import HashTableV8


class TestHashTable(unittest.TestCase):
    SIZE = 42

    def setUp(self):
        self.ht = HashTable(self.SIZE)
        # fill all but one position in table
        for i in range(self.SIZE - 1):
            self.ht[i] = i

    def test_hash(self):
        self.assertEqual(self.ht.hash(5), 5 % self.SIZE)
        self.assertEqual(self.ht.hash(42), 42 % self.SIZE)
        self.assertEqual(self.ht.hash('Rast'), 32)
        self.assertEqual(self.ht.hash('Star'), 30)
        print(test_hash(self))    
    def test_setitem(self):
        # basically it's one function for testing setitem and getitem
        # because they are interconnected and you can't really test getitem
        # without previously setting an item

        self.ht['Unicorns'] = ['does', 'not', 'exist']
        self.assertEqual(self.ht['Unicorns'], ['does', 'not', 'exist'])

        with self.assertRaises(KeyError):
            _ = self.ht['Not in table']

        with self.assertRaises(KeyError):
            self.ht['John'] = 'John'

        self.ht['Unicorns'] = 'of Love'
        self.assertEqual(self.ht['Unicorns'], 'of Love')

    def test_contains(self):
        self.assertEqual(0 in self.ht, True)
        self.assertEqual('Bobby' in self.ht, False)
        self.assertEqual(self.SIZE - 2 in self.ht, True)


class TestHashTableCollisions(unittest.TestCase):
    SIZE = 42

    def setUp(self):
        self.ht = HashTableV3(self.SIZE)

    def test_setget(self):
        # 6 is basically magic number for size of 42
        # if changing size, need to revise all test suite
        for i in range(0, self.SIZE * 6, 6):
            # testing setitem
            self.ht[i] = i

        self.assertEqual(self.ht[0], (0, 0, 0))
        self.assertEqual(self.ht[246], (246, 246, 6))
        self.assertEqual(self.ht[126], (126, 126, 4))

        with self.assertRaises(KeyError):
            _ = self.ht[self.SIZE + 1]

        with self.assertRaises(KeyError):
            _ = self.ht['Unicorn']


class TestProbing(unittest.TestCase):
    def test_probing(self):
        ht = HashTableV4(42)

        self.assertEqual(ht.probing(0, 0), 0)
        self.assertEqual(ht.probing(1, 10), 17)
        self.assertEqual(ht.probing(10, 34), 32)


class TestHashTableChained(unittest.TestCase):
    SIZE = 42

    def setUp(self):
        self.ht = HashTableV5(self.SIZE)

    def test_setget(self):
        # testing set
        try:
            for i in range(self.SIZE * 2):
                self.ht[i] = i
        except KeyError:
            self.fail('Unexpected KeyError.')

        self.assertEqual(self.ht[0], (0, 0))
        self.assertEqual(self.ht[self.SIZE - 1][0], self.SIZE - 1)
        self.assertEqual(self.ht[self.SIZE + 1], (self.SIZE + 1, 1))

        with self.assertRaises(KeyError):
            print(self.ht['John'])


class TestHashTableRehash(unittest.TestCase):
    SIZE = 42

    def setUp(self):
        self.hash_table = HashTableV8(self.SIZE)
        self.hash_table['John'] = 'John'

    def test_delete(self):
        self.assertEqual(self.hash_table['John'][1], 'John')
        self.hash_table.delete('John')
        with self.assertRaises(KeyError):
            print(self.hash_table['John'])
        with self.assertRaises(KeyError):
            self.hash_table.delete('John')

    def test_rehash(self):
        for i in range(self.SIZE - 1):
            self.hash_table[i] = i

        with self.assertRaises(ValueError):
            self.hash_table.rehash(0)

        with self.assertRaises(ValueError):
            self.hash_table.rehash(self.SIZE - 1)

        self.hash_table.rehash(self.SIZE + 1)
        self.assertEqual(self.hash_table.table_size, self.SIZE + 1)
        self.hash_table['Max'] = 'Max'
