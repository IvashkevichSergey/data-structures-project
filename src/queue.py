class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.list_of_data = []
        self.next_node_1 = None
        self.next_node_2 = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.next_node_2 = self.next_node_1
        self.next_node_1 = self.list_of_data[-1] if self.list_of_data else None
        self.list_of_data.append(data)
        self.tail = Node(data, None)
        self.head = Node(self.list_of_data[0], Node(self.next_node_1, self.next_node_2))

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return '\n'.join(self.list_of_data)
