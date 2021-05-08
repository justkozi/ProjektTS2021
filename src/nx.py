import networkx as nx
import matplotlib.pyplot as plt

master_color = []
slave_color = []
m_nodes = [
    "Dron na stanowisku startowym",
    "Proces sprawdzania stanu misji",
    "Proces powrotu i lądowania na stanowisku startowym",
    "Lot do kolejnego punktu kontrolnego z listy",
    "Proces sprawdzania obiektu na ziemi"
]

m_cords = {
    m_nodes[0]: (-0.5, 0),
    m_nodes[1]: (0, -1),
    m_nodes[2]: (-1, -1),
    m_nodes[3]: (-0.5, -2),
    m_nodes[4]: (0, -3)
}
m_edges = [
    (m_nodes[0], m_nodes[1]),
    (m_nodes[1], m_nodes[2]),
    (m_nodes[1], m_nodes[3]),
    (m_nodes[2], m_nodes[0]),
    (m_nodes[3], m_nodes[4]),
    (m_nodes[4], m_nodes[1])
]

s_nodes = [
    "Proces sprawdzania obiektu na ziemi",
    "Sprawdź jakiego koloru jest pole pod dronem",
    "Proces zrzutu kulek o kolorze A",
    "Proces zrzutu kulek o kolorze B",
    "Powrót do procesu głównego",
    "Wysyłaj informacje o błędzie zrzutu"
]

s_cords = {
    s_nodes[0]: (2, 0),
    s_nodes[1]: (1, 0),
    s_nodes[2]: (0, -1),
    s_nodes[3]: (0, 0),
    s_nodes[4]: (0, 1),
    s_nodes[5]: (-1, -0.5)
}

s_edges = [
    (s_nodes[0], s_nodes[1]),
    (s_nodes[1], s_nodes[2]),
    (s_nodes[1], s_nodes[3]),
    (s_nodes[1], s_nodes[4]),
    (s_nodes[2], s_nodes[4]),
    (s_nodes[2], s_nodes[5]),
    (s_nodes[3], s_nodes[4]),
    (s_nodes[3], s_nodes[5]),
    (s_nodes[4], s_nodes[0]),
    (s_nodes[5], s_nodes[4]),

]

m_options = {'node_color': master_color,
             'edge_color': 'black',
             'node_size': 20000,
             'width': 0.9,
             'with_labels': True,
             'pos': m_cords,
             'node_shape': 'o',
             'font_size': 6,
             }

s_options = {'node_color': slave_color,
             'edge_color': 'black',
             'node_size': 15000,
             'width': 0.9,
             'with_labels': True,
             'pos': s_cords,
             'node_shape': 'o',
             'font_size': 6,
             }

m = nx.DiGraph()
s = nx.DiGraph()

m.add_edges_from(m_edges)
m.add_nodes_from(m_nodes)

s.add_edges_from(s_edges)
s.add_nodes_from(s_nodes)


def draw_master(current_state):
    plt.ion()
    plt.figure('Proces główny', figsize=(10, 9))
    for node in m:
        if node == current_state:
            master_color.append('#FFA500')
        else:
            master_color.append('#C0C0C0')
    nx.draw(m, **m_options)
    plt.show()
    master_color.clear()
    plt.pause(1)

def draw_slave_graph(current_state):
    plt.ion()
    plt.figure('Proces podrzędny', figsize=(10, 9))
    for node in s:
        if node == current_state:
            slave_color.append('#FFA500')
        else:
            slave_color.append('#C0C0C0')

    nx.draw(s, **s_options)
    plt.show()
    slave_color.clear()
    plt.pause(1)