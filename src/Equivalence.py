from src.Automata import Automata
from src.MealyAutomata import MealyAutomata
from src.MooreAutomata import MooreAutomata
import src.Partition
class Equivalence:
    """
    Main class of the model it does the equivalence algorithm to test if 
    two automatas are equivalent 
    """

    EQUIVALENT_MACHINES = "They are equivalent"
    NOT_EQUIVALENT_MACHINES = "They are not equivalent"
    PRIMA = "`"

    def __init__(self, automata1, automata2):
        self.automata1 = automata1
        self.automata2 = automata2

    """
    Flow of the equivalence automatas algorithm:
    Remove unaccesible
    Rename same states
    Sum automatas
    First partition
    K+1 partition algorithm
    Check
    """
    def are_equivalent(self):
        #Remove unreachable vertices from two automatas
        self.automata1.remove_unreachable_vertices()
        self.automata2.remove_unreachable_vertices()

        #Rename same states
        if len(self.automata1.Q) >= len(self.automata2.Q):
            self.rename_states(self.automata1, self.automata2)
        else:
            self.rename_states(self.automata1, self.automata2)

        #Sum automatas
        automata = self.sum_automatas(self.automata1, self.automata2)

        #First partition
        first_partition = src.Partition.first_partition(automata)
        
        #Partitioning algorithm
        kplus1_partitions = src.Partition.kplus1partition(first_partition, [] , automata)

        #Check
        are_equivalent = self.validate_equivalence(self.automata1, self.automata2, kplus1_partitions)
        if are_equivalent:
            return self.EQUIVALENT_MACHINES
        else:
            return self.NOT_EQUIVALENT_MACHINES

    """
    The second automata will be the one that will be replaced
    We have to check first which one is bigger 
    """
    def rename_states(self, automata1, automata2):
        states_automata1 = automata1.state_map.keys()
        state_automata2 = automata2.state_map.keys()

        for state in state_automata2:
            if state in states_automata1:
                automata2.replace_state(state,state+self.PRIMA)

    def sum_automatas(self, automata1, automata2):
        Q = []
        state_map = {}
        transition_map = {}
        Q = automata1.Q + automata2.Q
        state_map = automata1.state_map
        state_map.update(automata2.state_map)
        transition_map = automata1.transition_map
        transition_map.update(automata2.transition_map)

        if isinstance(automata1, MooreAutomata):
            automata = MooreAutomata(Q, automata1.S, automata2.R, automata1.initial_state)
        else:
            automata = MealyAutomata(Q, automata1.S, automata2.R, automata1.initial_state)

        automata.state_map = state_map
        automata.transition_map = transition_map

        return automata

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
