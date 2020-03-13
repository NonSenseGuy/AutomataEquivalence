import unittest
from Automata import Automata

class Automata_Test(unittest.TestCase):

    def setup_moore_automata(self):
        self.automata = Automata(['A','B','C'],[0,1],[0,1],'A', "Moore")

    def test_add_state_moore(self):
        self.setup_moore_automata()
        self.automata.add_state('A', 0)
        self.assertEqual(self.automata.state_map['A'], [0], "No son iguales")
    def test_add_transition(self):
        self.setup_moore_automata()
        self.automata.add_state('A', 0)
        self.automata.add_state('B', 1)
        self.automata.add_transition(0,'A','B')
        self.assertEqual(self.automata.transition_map['A'], {(0,'B')})


automata = Automata(['A','B','C'],[0,1],[0,1],'A', "Moore")
print(automata.transition_map)