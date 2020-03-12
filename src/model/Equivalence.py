class Equivalence:
    """
    Main class of the model 
    """

    EQUIVALENT_MACHINES = "They are equivalent"
    NOT_EQUIVALENT_MACHINES = "They are not equivalent"

    def __init__(self, automata1, automata2):
        self.automata1 = automata1
        self.automata2 = automata2

    """
    The second automata will be the one that will be replaced
    We have to check first which one is bigger 
    """
    def rename_states(self, automata1, automata2):
        states_automata1 = automata1.S
        state_automata2 = automata2.S

        new_states = {}

        for state in state_automata2:
            new_states[state] = ""
            if state in states_automata1:
                new_states[state] = state+"'"
        
        automata2.replace_states(new_states)

    





