from Automata import Automata

class MooreAutomata(Automata):
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
        self.state_r = {}

    def add_state(self, q):
        try:
            if q in self.Q:
                self.transition_map[q] = set()
            else:
                raise ValueError
        except ValueError:
            print("El estado que se desea agregar no hacer parte del alfabeto de estados")
        
    
    def add_transition(self, stimuli, initial_q, final_q):
        try:
            if not initial_q in self.Q or not initial_q in self.state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in self.Q or not final_q in self.state_map.keys():
                raise ValueError("Estado final erroneo")

            self.state_map[initial_q].add(final_q)
        except ValueError:
            pass        

    def add_response(self,state, response):
        state_r[state] = response 


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
            del self.state_r[v]
            del self.state_map[v]
    
    def replace_states(self, new_states):
        pass 


