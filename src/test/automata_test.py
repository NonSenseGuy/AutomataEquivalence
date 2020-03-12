import unittest
from model import Automata

class Automata_Test(unittest.TestCase):

    def setup_moore_automata(self):
        self.automata = Automata(['A','B','C'],[0,1],[0,1], "Moore")

    def test_add_transition(self):
        self.setup_moore_automata()
        self.automata.add_transition(0,'A','B')
        self.assertEqual(Automata.transition_map['A'], (0,'B'))
