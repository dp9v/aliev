class Node:
    def __init__(self, next_node=None, value=0):
        self.__next_node = next_node
        self.value = value

    def is_last(self):
        return self.__next_node is None

    def has_next(self):
        return self.__next_node is not None

    def get_next(self):
        return self.__next_node

    def set_next(self, next_node):
        self.__next_node = next_node

    @classmethod
    def generate(cls, size=10):
        node = Node(value=size)
        for i in range(size, 0, -1):
            new_node = Node(node, i - 1)
            node = new_node
        return node

    def __str__(self):
        res = str(self.value)
        if not self.is_last():
            res += " -> " + str(self.get_next())
        return res

    def reverse(self):
        prev = None
        current = Node()
        current.set_next(self.get_next())
        current.value = self.value
        while current.has_next():
            tmp = current.get_next()
            current.set_next(prev)
            prev = current
            current = tmp
        current.set_next(prev)
        self.set_next(current.get_next())
        self.value = current.value


def _2_2(first: Node, k: int):
    res_node = first
    while not first.is_last():
        first = first.get_next()
        k -= 1
        if k <= 0:
            res_node = res_node.get_next()

    if k == 1:
        raise Exception()
    return res_node


ll = Node.generate(7)
print(ll)
ll.reverse()
print(ll)
