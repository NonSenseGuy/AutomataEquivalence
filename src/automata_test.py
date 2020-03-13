import unittest
from MealyAutomata import MealyAutomata

class MealyAutomata_Test(unittest.TestCase):

    def setup_mealy_automata(self):
        self.automata = MealyAutomata(['A','B','C'],[0,1],[0,1],'A')

    def add_state(self):
        self.setup_mealy_automata()
        self.automata.add_state('A')
        self.assertEqual(self.automata.state_map['A'], {}, "No son iguales")

    def test_add_transition(self):
        self.setup_mealy_automata()
        self.automata.add_state('A', 0)
        self.automata.add_state('B', 1)
        self.automata.add_transition(0,'A','B')
        self.assertEqual(self.automata.transition_map['A'], {(0,'B')})

