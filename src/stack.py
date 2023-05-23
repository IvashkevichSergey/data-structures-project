class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        # Верхний элемент стека
        self.top = None
        self.list_of_data = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)
        self.list_of_data.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        # Вызываем исключение когда стек пустой
        if not self.top:
            raise Exception('Стек пустой, удалять нечего')
        popped_data = self.top.data
        self.top = self.top.next_node
        self.list_of_data.pop()
        return popped_data

    def __str__(self):
        """
        Представление объекта класса при выводе на печать в виде строки
        с данными, имеющимися в стеке
        """
        return '\n'.join(self.list_of_data)
