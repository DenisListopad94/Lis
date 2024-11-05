import unittest
from .queue import Queue
# from django.test import TestCase


class UniqueQueue(unittest.TestCase):
    # storage = [1,2,3,4]



    def add(self):
        self.q = Queue('FIFO')
        if 4 not in self.q.storage:
            self.q.storage.append(4)
            # print(self.q.storage)

    def queue_length(self):
        self.q = Queue('FIFO')
        sum_len=len(self.q.storage)
        # print(sum_len)

    def last_added(self):
        self.q = Queue('LIFO')
        added = self.q.storage[-1]
        # print(added)

    def test_add(self):
        self.q = Queue('LIFO')
        if 5 not in self.q.storage:
            self.q.adds(5)
            self.assertEqual(self.q.storage[-1], 5)
            # print(self.storage)

    def test_not_add(self):
        self.q = Queue('LIFO')
        if 6 not in self.q.storage:
            self.q.adds(6)
            self.assertNotEqual(self.q.storage[-1], 1)

    # def test_not_add(self):
    #     self.q = self.storage
    #     if 6 not in self.q:
    #         self.q.append(6)
    #         self.assertNotEqual(self.q[-1], 1)
    #         print(self.storage)

    def test_not_len(self):
        self.q = Queue('FIFO')
        sum_len = len(self.q.storage)
        print(sum_len)
        self.assertNotEqual(sum_len, 2)

    def test_len(self):
        self.q = Queue('FIFO')
        sum_len = len(self.q.storage)
        print(sum_len)
        self.assertEqual(sum_len, 4)

    def test_false_bool(self):
        self.q = Queue('FIFO')
        sum_len = len(self.q.storage)
        self.assertFalse(not sum_len)

    def test_true_bool(self):
        self.q = Queue('FIFO')
        sum_len = len(self.q.storage)
        self.assertTrue(sum_len)

    def test_strategy_exist(self):
        self.q = Queue('FIFO')
        self.assertEqual(self.q.strategy, 'FIFO')

    def test_non_real_strategy(self):
        with self.assertRaises(TypeError):
            self.q = Queue('FIF')

    def test_add_elem_lifo(self):
        self.q = Queue('LIFO')
        self.q.adds(5)
        print(self.q.storage)
        self.q.adds(6)
        print(self.q.storage)
        self.q.adds(7)
        print(self.q.storage)
        first_elem = self.q.pop()
        print(self.q.storage)
        self.assertEqual(first_elem, 7)
        first_elem = self.q.pop()
        print(self.q.storage)
        self.assertEqual(first_elem, 6)
        first_elem = self.q.pop()
        print(self.q.storage)
        self.assertEqual(first_elem, 5)

    def test_add_elem_fifo(self):
        self.q = Queue('FIFO')
        self.q.add(8)
        print(self.q.storage)
        self.q.add(9)
        print(self.q.storage)
        self.q.add(10)
        print(self.q.storage)
        first_elem = self.q.pop1()
        self.assertEqual(first_elem, 8)
        print(self.q.storage)
        first_elem = self.q.pop2()
        self.assertEqual(first_elem, 9)
        print(self.q.storage)
        first_elem = self.q.pop3()
        self.assertEqual(first_elem, 10)
        print(self.q.storage)


if __name__ == '__main__':
    unittest.main()
