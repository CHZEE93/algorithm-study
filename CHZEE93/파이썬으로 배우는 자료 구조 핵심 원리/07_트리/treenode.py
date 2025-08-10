# 구현용
######################################################################
class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        return self.container[-1]


class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]


######################################################################


class TreeNode:

    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None

    def __del__(self):
        print("data {} is deleted".format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def data(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def data(self, right):
        self.__right = right

    def preorder(cur):
        if not cur:
            return

        print(cur.data, end=" ")

        preorder(cur.left)

        preorder(cur.right)

    def iter_preorder(cur):
        s = Stack()
        while True:
            while cur:
                print(cur.data, end=" ")
                s.push(cur)
                cur = cur.left

            cur = s.pop()
            if not cur:
                break

            cur = cur.right

    def inorder(cur):
        if not cur:
            return

        inorder(cur.left)

        print(cur.data, end=" ")

        inorder(cur.right)

    def iter_inorder(cur):
        s = Stack()
        while True:
            while cur:
                s.push(cur)
                cur = cur.left
            cur = s.pop()
            if not cur:
                break

            print(cur.data, end=" ")
            cur = cur.right

    def postorder(cur):
        if not cur:
            return

        postorder(cur.left)
        postorder(cur.right)
        print(cur.data, end=" ")

    def levelorder(cur):
        q = Queue()

        q.put(cur)
        while not q.empty():
            cur = q.get()
            print(cur.data, end=" ")
            if cur.left:
                q.put(cur.left)

            if cur.right:
                q.put(cur.right)
