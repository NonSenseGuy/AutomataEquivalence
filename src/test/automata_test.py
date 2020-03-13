from src.model.Automata import Automata
import unittest


class Automata_Test(unittest.TestCase):

    def setup_moore_automata(self):
        self.automata = Automata(['A','B','C'],[0,1],[0,1],'A', "Moore")

    def test_add_transition(self):
        self.setup_moore_automata()
        self.automata.add_transition(0,'A','B')
        self.assertEqual(self.automata.transition_map['A'], (0,'B'))
