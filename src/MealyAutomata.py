from Automata import Automata

class MealyAutomata(Automata):
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



    """

    def __init__(self, Q, S, R, initial_state):
        self.transition_map = {}    
        Automata.__init__(self, Q, S, R, initial_state)

    
    def add_state(self, q):
        try:
            if q in self.Q:
                self.state_map[q] = set()
                self.transition_map[q] = set()
            else:
                raise ValueError
        except ValueError:
            print("El estado que se desea agregar no hacer parte del alfabeto de estados")
    
    def add_transition(self, stimuli, initial_q, final_q, r):
        try:
            if not r in self.R:
                 raise ValueError("La respuesta no esta en el alfabeto de respuestas")
            if not initial_q in self.Q or not initial_q in self.state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in self.Q or not final_q in self.state_map.keys():
                raise ValueError("Estado final erroneo")

            self.transition_map[initial_q].add((stimuli,final_q, r)) 
            self.state_map[initial_q].add(final_q)
        except ValueError:
            pass        

    def add_response(self, stimuli, state, response):
        pass
    
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        for v in visited_vertices:
            del self.transition_map[v]
            del self.state_map[v]
    
    def replace_states(self, new_states):
        pass 


ma = MealyAutomata(['A','B','C'],[0,1],[0,1],'A')
ma.add_state('B')
ma.add_transition(0,'A','B',1)
print(ma.transition_map)