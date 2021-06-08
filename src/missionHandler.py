from random import random

from droneComm import *


def whatDo(state):
    if(state == str('Dron na stanowisku startowym')):
        start_mission()
        return str('m_0_1')
    elif(state == str('Proces sprawdzania stanu misji')):
        if(points_avalible()): return str('m_1_3')
        else: return str('m_1_2')
    elif(state == str('Lot do kolejnego punktu kontrolnego z listy')):
        fly_to_next()
        return str('m_3_4')
    elif(state == str('Podproces sprawdzania obiektu na ziemi')):
        return str('s_0_1')
    elif(state == str('Sprawdź jakiego koloru jest pole pod dronem')):
        col = check_current_colour()
        if(col == str('A')): return str('s_1_2')
        elif (col == str('B')): return str('s_1_3')
        else: return str('s_1_4')
    elif (state == str('Proces zrzutu kulek o kolorze A')):
        if(random() > 0.2):
            return str('s_2_5')
        else:
            return str('s_2_4')
    elif (state == str('Proces zrzutu kulek o kolorze B')):
        if (random() > 0.8):
            return str('s_3_5')
        else:
            return str('s_3_4')
    elif (state == str('Proces sprawdzania obiektu na ziemi')):
        return str('m_4_1')
    elif (state == str('Proces powrotu i lądowania na stanowisku startowym')):
        end_mission()
        # return str('m_2_0')
        return str('quit')
    elif (state == str('Wysyłaj informacje o błędzie zrzutu')):
        x = input("Wpisz [ok] oby zatwierdzić błąd zrzutu: ")
        if(x == str('ok')):
            return str('s_5_4')


