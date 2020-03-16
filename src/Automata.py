from src.AutomataInterface import AutomataInterface
from abc import ABC

class Automata(AutomataInterface):
    """
    A class used to represent an Automata wheter is a Moore automata or a Mealy automata
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
                self.transition_map[q] = []
            else:
                raise ValueError
        except ValueError:
            pass
        
    
    def add_transition(self):
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

