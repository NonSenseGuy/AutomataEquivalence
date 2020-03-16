from AutomataInterface import AutomataInterface
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
    
    """
    Q it is just the alphabet of states that you can use
    You need to add an state using this method to an automata 
    """
    def add_state(self, q):
        try:
            if q in self.Q:
                self.state_map[q] = set()
                self.transition_map[q] = []
            else:
                raise ValueError
        except ValueError:
            pass
        
    """
    It has its own implementation in Mealy and Moore automatas 
    """
    def add_transition(self):
        pass        

    """
    It has its own implementation in Mealy and Moore automatas 
    """
    def add_response(self, stimuli, state, response):
        pass

    """
    It is used to find the states that you can visit from the initial state
    """
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




