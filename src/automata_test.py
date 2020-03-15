import unittest
from MealyAutomata import MealyAutomata

class MealyAutomata_Test(unittest.TestCase):

    def setup_mealy_automata(self):
        self.automata = MealyAutomata(['A','B','C'],[0,1],[0,1],'A')

    def setup_mealy_automata_unreachable_vertices(self):
        self.setup_mealy_automata()
        self.automata.add_state('B')
        self.automata.add_state('C')
        self.automata.add_transition(0,'A', 'B', 1)
        self.automata.add_transition(0,'A', 'A', 0)
        self.automata.add_transition(0,'C', 'B', 1)

    ##To prove raise of value error exception when adding a state that is already on the automata
    def test_add_state_exception(self):
        self.setup_mealy_automata()
        self.automata.add_state('B')
        self.assertIn('B', self.automata.transition_map)


    ##To prove raise of value error exception when adding a state that is already on the automata
    def test_add_state_exception2(self):
        self.setup_mealy_automata()
        self.automata.add_state('D')
        self.assertRaises(ValueError)

    def test_add_transition(self):
        self.setup_mealy_automata()
        self.automata.add_state('A')
        self.automata.add_state('B')
        self.automata.add_transition(0,'A','B', 1)
        self.assertIn((0,'B',1), self.automata.transition_map['A'])

    def test_remove_unreachable_vertices(self):
        self.setup_mealy_automata_unreachable_vertices()
        self.automata.remove_unreachable_vertices()
        self.assertNotIn('C', self.automata.transition_map)