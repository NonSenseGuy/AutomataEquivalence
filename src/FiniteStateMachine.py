class FiniteStateMachine:
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
    FSM initial state

    """

    def __init__(self,Q,S,R,initial_state):
        map = {}
        self.Q = Q
        self.S = S 
        self.R = R
        self.initial_state = initial_state
    def add_state(self, q):
        pass
    
    def add_transition(self, stimuli, initial_s, final_s):
        pass

    def add_response(self, stimuli, state, response):
        pass

    







        

    

