from Automata import Automata


class Equivalence:
    """
    Main class of the model 
    """

    EQUIVALENT_MACHINES = "They are equivalent"
    NOT_EQUIVALENT_MACHINES = "They are not equivalent"
    PRIMA = "'"

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
                new_states[state] = state+PRIMA

        automata2.replace_states(new_states)

    def validate_equivalence(self, automata1, automata2, partitions):
        elements_in_partition = False
        initial_state = False

        states_automata1 = automata1.Q
        states_automata2 = automata2.Q

        initial_automata1 = automata1.initial_state
        initial_automata2 = automata2.initial_state

        for partition in partitions:
            union_1 = partition.intersection(states_automata1)
            union_2 = partition.intersection(states_automata2)

            if initial_automata1 in partition:
                if initial_automata2 in partition:
                    initial_state = True
                else:
                    return initial_state

            if len(union_1) == 0 or len(union_2) == 0:
                return elements_in_partition

        elements_in_partition = True
        return (elements_in_partition and initial_state)

