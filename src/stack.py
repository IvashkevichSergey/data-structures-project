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
        # Список узлов стека
        self.node_list = []
        # Верхний элемент стека
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        # Определяем второй элемент узла стека
        second_element = None if len(self.node_list) < 1 else self.node_list[-1]
        # Определяем узел стека на вершине стека
        self.top = Node(data, second_element)
        # Добавляем новый узел в список узлов стека
        self.node_list.append(self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        pass
