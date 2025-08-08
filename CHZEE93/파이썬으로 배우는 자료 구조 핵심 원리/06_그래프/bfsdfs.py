from queue import Queue


# 구현용
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


class Graph:
    def __init__(self, vertex_num):
        self.adj_list = [[] for _ in range(vertex_num)]
        self.visited = [False for _ in range(vertex_num)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def bfs(self, v):
        q = Queue()
        self.init_visited()

        q.put(v)
        self.visited[v] = True

        while not q.empty():
            v = q.get()
            print(v, end=" ")
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    q.put(u)
                    self.visited[u] = True

    def __dfs_recursion(self, v):
        print(v, end=" ")
        self.visited[v] = True

        adj_v = self.adj_list[v]
        for u in adj_v:
            if not self.visited[u]:
                self.__dfs_recursion(u)

    def dfs(self, v):
        self.init_visited()
        self.__dfs_recursion(v)

    def iter_dfs(self, v):
        s = Stack()
        self.init_visited()

        s.push(v)
        self.visited[v] = True
        print(v, end=" ")

        is_visited = False

        while not len(s) == 0:
            is_visited = False
            v = s.peek()
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    s.push(u)
                    self.visited[u] = True
                    print(u, end=" ")
                    is_visited = True
                    break

        if not is_visited:
            s.pop()

    def dfs_all(self):
        self.init_visited()

        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.__dfs_recursion(i)
