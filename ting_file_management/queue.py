from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def search(self, index):
        if index >= 0 and index < self.size():
            return self._data[index]
        else:
            raise IndexError('Índice Inválido ou Inexistente')

    def is_empty(self):
        return self._data == []

    def size(self):
        return len(self._data)
