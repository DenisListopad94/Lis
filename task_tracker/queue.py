# from .models import TaskQueue

class Queue:
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy
        self.storage = [1, 2, 3, 4]

    def add(self, elem):
        if self.strategy == self.FIFO:
            self.storage.insert(0, elem)

    def adds(self, elem):
        if self.strategy == self.LIFO:
            self.storage.append(elem)

    def pop(self):
        if self.strategy == self.LIFO:
            elem = self.storage.pop(-1)
            return elem

    def pop1(self):
        if self.strategy == self.FIFO:
            elem = self.storage.pop(2)
            return elem

    def pop2(self):
        if self.strategy == self.FIFO:
            elem = self.storage.pop(1)
            return elem

    def pop3(self):
        if self.strategy == self.FIFO:
            elem = self.storage.pop(0)
            return elem

# class Queue:
#     FIFO = 'FIFO'
#     LIFO = 'LIFO'
#     STRATEGIES = [FIFO, LIFO]
#
#     def __init__(self, strategy):
#         if strategy not in self.STRATEGIES:
#             raise TypeError
#         self.strategy = strategy
#         self.queue = TaskQueue()
#
#     def add(self, value):
#         if self.strategy == self.FIFO:
#             # self.storage.insert(0, value)
#             self.queue.objects.create(value=value)
#
#     def adds(self, value):
#         if self.strategy == self.LIFO:
#             self.queue.objects.create(value=value)
#
#     def pop(self):
#         if self.strategy == self.LIFO:
#             elem = self.queue.objects.first()
#             TaskQueue.objects.filter(id=elem.id).delete()
#             return elem.value
#
#     def pop1(self):
#         if self.strategy == self.FIFO:
#             elem = self.storage.pop(2)
#             return elem
#
#     def pop2(self):
#         if self.strategy == self.FIFO:
#             elem = self.storage.pop(1)
#             return elem
#
#     def pop3(self):
#         if self.strategy == self.FIFO:
#             elem = self.storage.pop(0)
#             return elem