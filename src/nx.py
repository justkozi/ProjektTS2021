import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Process

plt.ion()
fig = plt.figure()
fig.set_size_inches(16, 8)


def draw_graph(state):
    plt.clf()
    master_color = []
    slave_color = []
    m_nodes = [
        "Dron na stanowisku startowym",
        "Proces sprawdzania stanu misji",
        "Proces powrotu i lądowania na stanowisku startowym",
        "Lot do kolejnego punktu kontrolnego z listy",
        "Proces sprawdzania obiektu na ziemi"
    ]

    m_nodes_alt_name = [
        "Dron na \nstanowisku startowym",
        "Proces sprawdzania \nstanu misji",
        "Proces powrotu \ni lądowania na \nstanowisku startowym",
        "Lot do kolejnego punktu \nkontrolnego z listy",
        "Proces sprawdzania \nobiektu na ziemi"
    ]

    m_nodes_relab = {
        m_nodes[0]: m_nodes_alt_name[0],
        m_nodes[1]: m_nodes_alt_name[1],
        m_nodes[2]: m_nodes_alt_name[2],
        m_nodes[3]: m_nodes_alt_name[3],
        m_nodes[4]: m_nodes_alt_name[4]
    }

    m_cords = {
        m_nodes_alt_name[0]: (-0.5, 0),
        m_nodes_alt_name[1]: (0, -1),
        m_nodes_alt_name[2]: (-1, -1),
        m_nodes_alt_name[3]: (-0.5, -2),
        m_nodes_alt_name[4]: (0, -3)
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

    s_nodes_alt_name = [
        "Proces sprawdzania \nobiektu na ziemi",
        "Sprawdź jakiego \nkoloru jest pole \npod dronem",
        "Proces zrzutu \nkulek o kolorze A",
        "Proces zrzutu \nkulek o kolorze B",
        "Powrót do \nprocesu głównego",
        "Wysyłaj informacje \no błędzie zrzutu"
    ]

    s_nodes_relab = {
        s_nodes[0]: s_nodes_alt_name[0],
        s_nodes[1]: s_nodes_alt_name[1],
        s_nodes[2]: s_nodes_alt_name[2],
        s_nodes[3]: s_nodes_alt_name[3],
        s_nodes[4]: s_nodes_alt_name[4],
        s_nodes[5]: s_nodes_alt_name[5]
    }

    s_cords = {
        s_nodes_alt_name[0]: (2, 0),
        s_nodes_alt_name[1]: (1, 0),
        s_nodes_alt_name[2]: (0, -1),
        s_nodes_alt_name[3]: (0, 0),
        s_nodes_alt_name[4]: (0, 1),
        s_nodes_alt_name[5]: (-1, -0.5)
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
                 'node_size': 4500,
                 'width': 0.9,
                 'with_labels': True,
                 'pos': m_cords,
                 'node_shape': 'o',
                 'font_size': 6,
                 }

    s_options = {'node_color': slave_color,
                 'edge_color': 'black',
                 'node_size': 4500,
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

    for node in m:
        if node == state:
            master_color.append('#FFA500')
        else:
            master_color.append('#C0C0C0')

    for node in s:
        if node == state:
            slave_color.append('#FFA500')
        else:
            slave_color.append('#C0C0C0')

    plt.subplot(121)
    m = nx.relabel_nodes(m, m_nodes_relab)
    nx.draw(m, **m_options)

    plt.subplot(122)
    s = nx.relabel_nodes(s, s_nodes_relab)
    nx.draw(s, **s_options)
    plt.draw()
    plt.pause(0.1)
    plt.clf()


def draw_graphs():
    p = Process(target=draw_graphs())
    p.start()
    p.join()
