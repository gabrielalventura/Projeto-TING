from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index >= 0 and index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self._data) == 0

# funções baseadas no repositório da aula 3.4 e
# no material do course do dia 3.4
# referência para buscas :
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
