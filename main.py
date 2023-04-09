import math
import networkx as nx
import matplotlib.pyplot as plt
import time
import random
import warnings

warnings.filterwarnings("ignore")

rates1 = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]

rates2 = [
    [1, 0.25, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.90, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 72.4, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.30],
    [0.20, 0.047, 0.052, 3.33, 3.60, 1],
]


rates3 = [
    [1, 0.37, 0.25, 16.43, 18.21, 3.94],
    [4.34, 1, 1.11, 71.40, 70.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.40, 1],
]

rates4 = [
    [1, 0.23, 0.45, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 72.40, 79.09, 29.44],
    [3.93, 0.90, 1, 64.52, 75.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]


rates5 = [
    [1, 0.23, 0.25, 16.43, 20.21, 4.94],
    [4.34, 1, 1.71, 71.40, 79.09, 21.44],
    [3.93, 0.93, 1, 64.52, 71.48, 19.37],
    [0.0061, 0.014, 0.015, 1, 1.21, 0.30],
    [0.055, 0.013, 0.018, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]


rates6 = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [7.93, 0.98, 1, 65.52, 74.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.39],
    [0.045, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]


rates7 = [
    [1, 0.23, 0.25, 20.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 15.37],
    [0.061, 0.014, 0.025, 1, 1.11, 0.23],
    [0.075, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.032, 3.33, 3.69, 1],
]

arr_rates = [rates1, rates2, rates3, rates4, rates5, rates6, rates7]

numb_to_currencies = {0: 'RUB', 1: 'USD', 2: 'EUR', 3: 'GBP', 4: 'BYN', 5: 'CNY'}
currencies_to_numb = {'RUB': 0, 'USD': 1, 'EUR': 2, 'GBP': 3, 'BYN': 4, 'CNY': 5}


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

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


def logarithm_convertor(graph):
    result = [[math.log(edge) for edge in row] for row in graph]
    return result


def fill_graph(rates, graph):
    size = len(rates)
    for i in range(size):
        for j in range(size):
            if i != j:
                graph.addEdge(i, j, rates[i][j])


def print_graf(cycle):
    G = nx.Graph()
    G.add_nodes_from([numb_to_currencies[i] for i in range(len(numb_to_currencies))])
    node_color = ["green"] * 6
    edge_color = ["black"] * 15
    G.add_edges_from([
        ("GBP", "EUR"),
        ("GBP", "USD"),
        ("GBP", "RUB"),
        ("GBP", "BYN"),
        ("GBP", "CNY"),
        ("EUR", "USD"),
        ("EUR", "RUB"),
        ("EUR", "BYN"),
        ("EUR", "CNY"),
        ("USD", "RUB"),
        ("USD", "BYN"),
        ("USD", "CNY"),
        ("RUB", "BYN"),
        ("RUB", "CNY"),
        ("BYN", "CNY"),
    ])

    edge_labels = {
        ("GBP", "EUR"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["EUR"]]),
        ("GBP", "USD"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["USD"]]),
        ("GBP", "RUB"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["RUB"]]),
        ("GBP", "BYN"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["BYN"]]),
        ("GBP", "CNY"): str(rates[currencies_to_numb["GBP"]][currencies_to_numb["CNY"]]),
        ("EUR", "USD"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["USD"]]),
        ("EUR", "RUB"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["RUB"]]),
        ("EUR", "BYN"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["BYN"]]),
        ("EUR", "CNY"): str(rates[currencies_to_numb["EUR"]][currencies_to_numb["CNY"]]),
        ("USD", "RUB"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["RUB"]]),
        ("USD", "BYN"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["BYN"]]),
        ("USD", "CNY"): str(rates[currencies_to_numb["USD"]][currencies_to_numb["CNY"]]),
        ("RUB", "BYN"): str(rates[currencies_to_numb["RUB"]][currencies_to_numb["BYN"]]),
        ("RUB", "CNY"): str(rates[currencies_to_numb["RUB"]][currencies_to_numb["CNY"]]),
        ("BYN", "CNY"): str(rates[currencies_to_numb["BYN"]][currencies_to_numb["CNY"]]),
    }

    options = {
        'node_size': 3500,
        'width': 1,
        'arrowstyle': '-|>',
        'arrowsize': 18,
    }

    node_color[currencies_to_numb[chosen_currency]] = 'yellow'
    for element in cycle:
        node_color[element] = 'yellow'

    if cycle[0] != currencies_to_numb[chosen_currency]:
        pos = nx.circular_layout(G)
        node_color[currencies_to_numb[chosen_currency]] = 'red'
        nx.draw_circular(G, node_color=node_color, edge_color=edge_color, with_labels=True, **options)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='blue')
        plt.show()
        node_color[currencies_to_numb[chosen_currency]] = 'yellow'
        time.sleep(0.1)

    for element in cycle:
        pos = nx.circular_layout(G)
        node_color[element] = 'red'
        nx.draw_circular(G, node_color=node_color, edge_color=edge_color, with_labels=True, **options)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='blue')
        plt.show()
        node_color[element] = 'yellow'
        time.sleep(0.1)

    if cycle[0] != currencies_to_numb[chosen_currency]:
        pos = nx.circular_layout(G)
        node_color[currencies_to_numb[chosen_currency]] = 'red'
        nx.draw_circular(G, node_color=node_color, edge_color=edge_color, with_labels=True, **options)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='blue')
        plt.show()
        node_color[currencies_to_numb[chosen_currency]] = 'yellow'
        time.sleep(0.1)


def earn_money(money, cycle):
    start = currencies_to_numb[chosen_currency]
    end = cycle[0]
    for i in range(1, len(cycle) + 1):
        money *= rates[start][end]
        start = end
        if i < len(cycle):
            end = cycle[i]
    money *= rates[start][currencies_to_numb[chosen_currency]]
    return money


print("Please, choose the currency from the list: \n 1) RUB \n 2) USD \n 3) EUR \n 4) GBP \n 5) BYN \n 6) CNY ")
chosen_currency = input().upper()
if chosen_currency.isdigit():
    chosen_currency = numb_to_currencies[int(chosen_currency) - 1]

print("Enter an initial amount:", end=' ')
money = int(input())

count_v = len(numb_to_currencies)
count_e = math.comb(count_v, 2) * 2
random_time_stop = random.randrange(1, len(arr_rates))

for i in range(random_time_stop):
    rates = arr_rates[i]
    log_rates = logarithm_convertor(rates)

    graph = Graph(count_v)
    fill_graph(log_rates, graph)

    cycle = list(graph.negative_cycle(currencies_to_numb[chosen_currency]))

    if graph.is_negative_cycle(currencies_to_numb[chosen_currency]):
        print_graf(cycle)
        money = earn_money(money, cycle)
print(f"Your balance: {money} {chosen_currency}")

