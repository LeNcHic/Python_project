class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # check is there a negative cycle in graph
    def is_negative_cycle(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return True

        return False

    # find negative cycle in the graph
    def negative_cycle(self, src):
        dist = [float("Inf")] * self.V
        arr = [-1] * self.V
        dist[src] = 0
        ans = []
        x = -1
        for i in range(0, self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    arr[v] = u
                    x = v
        if x == -1:
            print("No cycle")
        else:
            y = x
            for i in range(self.V):
                y = arr[y]
            cur = y
            while True:
                ans.append(cur)
                if cur == y and len(ans) > 1:
                    break
                cur = arr[cur]

            return reversed(ans)

    # complete graph with data from rates
    def fill_graph(self, rates):
        size = len(rates)
        for i in range(size):
            for j in range(size):
                if i != j:
                    self.add_edge(i, j, rates[i][j])
