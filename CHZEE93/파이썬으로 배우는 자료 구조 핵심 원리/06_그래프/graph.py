class Graph:
    def __init__(self, vertex_num=None):
        self.adj_list = []  # 인접리스트
        self.vtx_num = 0
        self.vtx_arr = []  # 있으면 True 없으면 False

        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]
            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False

    def add_vertex(self):  # 추가된 정점의 인덱스 반환
        for i in range(len(self.vtx_arr)):
            if self.vtx_arr[i] == False:  # 삭제된 경우
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i

        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1

    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")

        if self.vtx_arr[v]:
            self.adj_list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False

            for adj in self.adj_list:
                for vertex in adj:
                    if vertex == v:
                        adj.remove(vertex)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def delete_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self, v):
        return self.adj_list[v]
