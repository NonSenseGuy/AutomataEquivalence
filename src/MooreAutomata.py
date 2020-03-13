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
        self.transition_map = {}
        Automata.__init__(self, Q, S, R, initial_state)
            
    
    def add_transition(self, stimuli, initial_q, final_q):
        try:
            if not initial_q in self.Q or not initial_q in self.state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in self.Q or not final_q in self.state_map.keys():
                raise ValueError("Estado final erroneo")

            self.state_map[initial_q].add(final_q)
            self.transition_map[initial_q].add((stimuli, final_q))
        except ValueError:
            pass        

    def add_response(self,state, response):
        try:
            if not response in self.R: 
                raise ValueError("La respuesta no esta contenida en el alfabeto de respuestas")
            self.state_r[state] = response 
        except ValueError:
            pass

    
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        for v in visited_vertices:
            del self.state_r[v]
            del self.state_map[v]
    
    def replace_states(self, new_states):
        pass 


ma = MooreAutomata(['A','B','C'],[0,1],[0,1],'A')
ma.add_state('B')
ma.add_transition(0,'A','B')
print(ma.state_map)