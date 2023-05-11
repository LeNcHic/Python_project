import networkx as nx
import matplotlib.pyplot as plt
import time
import src.elements_for_printing_graph as elm
import src.connection_number_curr as connect


def colour_the_start_of_cycle(G, node_color, edge_labels, edge_color, options, cycle, chosen_currency):
    if cycle[0] != connect.currencies_to_numb[chosen_currency]:
        pos = nx.circular_layout(G)
        node_color[connect.currencies_to_numb[chosen_currency]] = 'red'
        nx.draw_circular(G, node_color=node_color, edge_color=edge_color, with_labels=True, **options)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='blue')
        plt.show()
        node_color[connect.currencies_to_numb[chosen_currency]] = 'yellow'
        time.sleep(0.1)


def print_graf(rates, cycle, chosen_currency):
    G = nx.Graph()
    G.add_nodes_from([connect.numb_to_currencies[i] for i in range(len(connect.numb_to_currencies))])
    node_color = ["green"] * 6
    edge_color = ["black"] * 15

    G.add_edges_from(elm.edges)
    edge_labels = elm.get_edge_labels(rates, connect.currencies_to_numb)

    options = {
        'node_size': 3500,
        'width': 1,
        'arrowstyle': '-|>',
        'arrowsize': 18,
    }

    node_color[connect.currencies_to_numb[chosen_currency]] = 'yellow'
    start = chosen_currency
    for i in range(len(cycle)):
        node_color[cycle[i]] = 'yellow'
        if start != connect.numb_to_currencies[cycle[i]]:
            edge_color[elm.edge_to_numb[(start, connect.numb_to_currencies[cycle[i]])]] = 'yellow'
        start = connect.numb_to_currencies[cycle[i]]

    if chosen_currency != start:
        edge_color[elm.edge_to_numb[(chosen_currency, start)]] = 'yellow'

    colour_the_start_of_cycle(G, node_color, edge_labels, edge_color, options, cycle, chosen_currency)

    for element in cycle:
        pos = nx.circular_layout(G)
        node_color[element] = 'red'
        nx.draw_circular(G, node_color=node_color, edge_color=edge_color, with_labels=True, **options)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_color='blue')
        plt.show()
        node_color[element] = 'yellow'

    colour_the_start_of_cycle(G, node_color, edge_labels, edge_color, options, cycle, chosen_currency)
