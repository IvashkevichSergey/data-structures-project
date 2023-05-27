class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
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

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        # Если очередь пустая - задаем одно и то же значение и для
        # начала и для конца очереди
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
        Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        # Если данных в очереди нет - возвращает пустую строку
        if not self.head:
            return ''
        tmp_var = self.head
        list_of_data = [self.head.data]
        # Добавляем в список имеющиеся в очереди данные до тех пор,
        # пока next_node не будет иметь значение None
        while tmp_var.next_node:
            tmp_var = tmp_var.next_node
            list_of_data.append(tmp_var.data)
        return '\n'.join(list_of_data)
