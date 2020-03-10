class Automata:
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

    MEALY = "Mealy"
    MOORE = "Moore"

    def __init__(self,Q,S,R,initial_state, automata_type):
        self.automata_type = automata_type
        self.state_map = {}
        self.transition_map = {}
        self.Q = Q
        self.S = S 
        self.R = R
        self.initial_state = initial_state
        
    def add_state(self, q, r):
        state_map[q] = [r]
        transition_map[q] = []
    
    def add_transition(self, stimuli, initial_q, final_q):
        transition_map[initial_q].append((stimuli,final_q)) 

    def add_response(self, stimuli, state, response):
        pass

    def find_inaccesible_vertices(self):
        pass







        

    

