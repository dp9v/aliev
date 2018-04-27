class Node:
    def __init__(self, next_node=None, value = 0):
        self.__next_node = next_node
        self.value = value

    def is_last(self):
        return self.__next_node is None

    def get_next(self):
        return self.__next_node

    @classmethod
    def generate(cls, size=10):
        node = Node(value=size)
        for i in range(size, 0, -1):
            new_node = Node(node, i-1)
            node = new_node
        return node

    def __str__(self):
        res = str(self.value)
        if not self.is_last():
            res += " -> "+str(self.get_next())
        return res


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
print(_2_2(ll, 3))
print(_2_2(ll, 7))
print(_2_2(ll, 4))