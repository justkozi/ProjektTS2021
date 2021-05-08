from statemachine import State
from nx import *
from transitions import *
from generator import *


def is_valid(available_states, test_state):
    for state in available_states.transitions:
        if state.identifier == test_state:
            return True
    return False


def show_moves(state):
    for trans in transition_names:
        for transition in state.transitions:
            if (trans['transition'] == transition.identifier):
                print(transition.identifier, "-", trans['name'])


master = [
    {"name": "Dron na stanowisku startowym",  # 0
     "initial": True,
     "value": "dron_start"},

    {"name": "Proces sprawdzania stanu misji",  # 1
     "initial": False,
     "value": "sprawdzanie_stanu_misji"},

    {"name": "Proces powrotu i lądowania na stanowisku startowym",  # 2
     "initial": False,
     "value": "powrot_na_start"},

    {"name": "Lot do kolejnego punktu kontrolnego z listy",  # 3
     "initial": False,
     "value": "lot_kolejny_punkt"},

    {"name": "Proces sprawdzania obiektu na ziemi",  # 4
     "initial": False,
     "value": "sprawdzanie_obiektu"}
]

slave = [
    {"name": "Proces sprawdzania obiektu na ziemi",  # 0
     "initial": True,
     "value": "sprawdzanie_obiektu"},

    {"name": "Sprawdź jakiego koloru jest pole pod dronem",  # 1
     "initial": False,
     "value": "sprawdz_kolor_pod_dronem"},

    {"name": "Proces zrzutu kulek o kolorze A",  # 2
     "initial": False,
     "value": "zrzut_a"},

    {"name": "Proces zrzutu kulek o kolorze B",  # 3
     "initial": False,
     "value": "zrzut_b"},

    {"name": "Powrót do procesu głównego",  # 4
     "initial": False,
     "value": "powrot_glowny_proces"},

    {"name": "Wysyłaj informacje o błędzie zrzutu",  # 5
     "initial": False,
     "value": "blad_zrzutu"}
]

transition_names = [
    {"transition": "m_0_1",
     "name": "Rozpoczęcie misji"},
    {"transition": "m_1_2",
     "name": "Lista punktów do odwiedzenia jest pusta"},
    {"transition": "m_1_3",
     "name": "Lista punktów do odwiedzenia nie jest pusta"},
    {"transition": "m_3_4",
     "name": "Osiągnięcie docelowego punktu"},
    {"transition": "m_2_0",
     "name": "Powrót do stanowiska początkowego"},
    {"transition": "m_4_1",
     "name": "Usuń obecny punkt z listy do odwiedzenia"},
    {"transition": "s_0_1",
     "name": "Uruchom proces sprawdzania koloru"},
    {"transition": "s_1_2",
     "name": "Pole jest koloru A"},
    {"transition": "s_1_3",
     "name": "Pole jest koloru B"},
    {"transition": "s_1_4",
     "name": "Pole jest innego koloru"},
    {"transition": "s_2_4",
     "name": "Zrzut prawidłowy"},
    {"transition": "s_3_4",
     "name": "Zrzut prawidłowy"},
    {"transition": "s_2_5",
     "name": "Błąd zrzutu"},
    {"transition": "s_3_5",
     "name": "Błąd zrzutu"},
    {"transition": "s_5_4",
     "name": "Manualne zatwierdzenie błędu"}
]

# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in master]
slave_states = [State(**opt) for opt in slave]

# valid transitions for a master (indices of states from-to)
master_from_to = [
    [0, [1]],
    [1, [2, 3]],
    [2, [0]],
    [3, [4]],
    [4, [1]]
]

slave_from_to = [
    [0, [1]],
    [1, [2, 3, 4]],
    [2, [4, 5]],
    [3, [4, 5]],
    [4, [0]],
    [5, [4]]
]

slave_states, slave_transitions = setTransition(slave_from_to, slave_states, 's')
master_states, master_transitions = setTransition(master_from_to, master_states, 'm')

master = Generator.create_master(master_states, master_transitions)
slave = Generator.create_master(slave_states, slave_transitions)

current_master = master
current_master_state = 0
current_slave_state = 0

print("********START************")
print("Aby dokonać przejscia podaj wartosc z ktorej tranzycji_do ktorej tranzycji, aby wyjsc wpisz quit")
print("--------------------------")

while True:
    print("--------------------------")
    print("Twój aktualny stan:")
    print(current_master.current_state.name)
    print("--------------------------")
    print("Twoje obecne możliwe tranzycje to:")
    show_moves(current_master.current_state)
    print("-------------------")
    if current_master == master:
        draw_master(current_master.current_state.name)
    else:
        draw_slave_graph(current_master.current_state.name)

    x = input("Wpisz wybrana tranzycje: ")
    if x == str('quit'):
        break
    elif is_valid(current_master.current_state, x):
        if x == str('quit'):
            break
        elif x == str("m_3_4"):
            print("Przejście do podprocesu")
            master_transitions[x]._run(current_master)
            current_master = slave
            continue
        elif x == str("s_1_4") or x ==  str("s_2_4") or x == str("s_3_4"):
            print("Powrót do głównego procesu")
            slave_transitions[x]._run(current_master)
            slave_transitions['s_4_0']._run(current_master)
            current_master = master
            continue

        if current_master == master:
            master_transitions[x]._run(current_master)
        else:
            slave_transitions[x]._run(current_master)
    else:
        print("Zła wartość!, aby wyjść wpisz quit")
print("-------------------")
print("Nastąpiło wyjście z programu")
print("-------------------")
