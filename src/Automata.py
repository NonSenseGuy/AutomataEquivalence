from AutomataInterface import AutomataInterface
from abc import ABC

class Automata(AutomataInterface):
    """
    A class used to represent a deterministic finite state machine

    ...

    Attributes
    ----------
    Q : list(str)
    State set
    S : list(str)
    Stimuli set
    R : list(str):
    Response set
    initial_state : str
    Automata initial state
    automata_type : str
    Automate type can be mealy or moore



    """

    def __init__(self, Q, S, R, initial_state):
        self.state_map = {}
        self.Q = Q
        self.S = S
        self.R = R
        self.initial_state = initial_state
        self.add_state(initial_state)
    

    def add_state(self, q):
        try:
            if q in self.Q:
                self.state_map[q] = set()
            else:
                raise ValueError
        except ValueError:
            print("El estado que se desea agregar no hacer parte del alfabeto de estados")
        
    
    def add_transition(self, stimuli, initial_q, final_q, r):
        try:
            if not r in R:
                 raise ValueError("La respuesta no esta en el alfabeto de respuestas")
            if not initial_q in Q or not initial_q in state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in Q or not final_q in state_map.keys():
                raise ValueError("Estado final erroneo")

            self.transition_map[initial_q].add((stimuli,final_q, r)) 
            self.state_map[initial_q].add(final_q)
        except ValueError:
            pass        

    def add_response(self, stimuli, state, response):
        pass

    def bfs(self):
        visited, queue = set(), [self.initial_state]
        while queue:
            vertex = queue.pop()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.state_map[vertex] - visited)
        return visited
    
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        for v in visited_vertices:
            del self.transition_map[v]
            del self.state_map[v]
    
    def replace_states(self, new_states):
        pass 


"""
Eliminar innacesibles
Renombrar mismo nombre
Sumar automatas
Particion 1
Hacer el algoritmo
Verificar Done
"""

