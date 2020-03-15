import unittest
from MealyAutomata import MealyAutomata

class MealyAutomata_Test(unittest.TestCase):

    def setup_mealy_automata(self):
        self.automata = MealyAutomata(['A','B','C'],[0,1],[0,1],'A')

    ##To prove raise of value error exception when adding a state that is already on the automata
    def test_add_state_exception(self):
        self.setup_mealy_automata()
        self.automata.add_state('A')
        self.assertRaises(ValueError)


    ##To prove raise of value error exception when adding a state that is already on the automata
    def test_add_state_exception2(self):
        self.setup_mealy_automata()
        self.automata.add_state('D')
        self.assertRaises(ValueError)

    def test_add_transition(self):
        self.setup_mealy_automata()
        self.automata.add_state('A', 0)
        self.automata.add_state('B', 1)
        self.automata.add_transition(0,'A','B')
        self.assertEqual(self.automata.transition_map['A'], {(0,'B')})

