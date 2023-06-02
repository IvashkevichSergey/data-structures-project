class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в начало связанного списка"""
        node = Node(data)
        # Если список пустой - задаем одно и то же значение и для
        # начала и для конца списка
        if not self.head:
            self.head = self.tail = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными
        в конец связанного списка"""
        node = Node(data)
        # Если список пустой - задаем одно и то же значение и для
        # начала и для конца списка
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
