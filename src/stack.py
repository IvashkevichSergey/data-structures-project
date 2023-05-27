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

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

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
        return popped_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        # Если данных в очереди нет - возвращает пустую строку
        if not self.top:
            return ''
        tmp_var = self.top
        list_of_data = [self.top.data]
        # Добавляем в список имеющиеся в очереди данные до тех пор,
        # пока next_node не будет иметь значение None
        while tmp_var.next_node:
            tmp_var = tmp_var.next_node
            list_of_data.append(tmp_var.data)
        return '\n'.join(list_of_data)
