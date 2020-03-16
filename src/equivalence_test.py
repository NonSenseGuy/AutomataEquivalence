import unittest
import src.Partition
from Automata import Automata
from Equivalence import Equivalence
from MealyAutomata import MealyAutomata

class Equivalence_Test(unittest.TestCase):

    def set_up_automata(self):
        self.automata1 = MealyAutomata(['A', 'B', 'C'], ['a','b'], [0,1], 'A')
        self.automata1.add_state('B')
        self.automata1.add_state('C')
        self.automata1.add_transition('a', 'A', 'C', 0)
        self.automata1.add_transition('a', 'B', 'C', 0)
        self.automata1.add_transition('a', 'C', 'B', 0)
        self.automata1.add_transition('b', 'A', 'B', 0)
        self.automata1.add_transition('b', 'B', 'A', 1)
        self.automata1.add_transition('b', 'C', 'C', 0)

        self.automata2 = MealyAutomata(['W', 'X', 'Y', 'Z'], ['a','b'], [0,1], 'W')
        self.automata2.add_state('X')
        self.automata2.add_state('Y')
        self.automata2.add_state('Z')
        self.automata2.add_transition('a', 'W', 'Z', 0)
        self.automata2.add_transition('a', 'X', 'Z', 0)
        self.automata2.add_transition('a', 'Y', 'Z', 0)
        self.automata2.add_transition('a', 'Z', 'Y', 0)
        self.automata2.add_transition('b', 'W', 'X', 0)
        self.automata2.add_transition('b', 'X', 'W', 1)
        self.automata2.add_transition('b', 'Y', 'W', 1)
        self.automata2.add_transition('b', 'Z', 'Z', 0)

        self.equivalence = Equivalence(self.automata1, self.automata2)

    def set_up_validate_equivalence(self):
        self.set_up_automata()
        self.partitions = []
        self.partition = set()
        self.partition.add('A')
        self.partition.add('W')
        self.partitions.append(self.partition)
        self.partition = set()
        self.partition.add('C')
        self.partition.add('Z')
        self.partitions.append(self.partition)
        self.partition = set()
        self.partition.add('B')
        self.partition.add('X')
        self.partition.add('Y')
        self.partitions.append(self.partition)

    ##To prove the comparision between two states are in the same partition or not 
    def test_sum_automata(self):
        self.set_up_automata()
        self.summedautomata = self.equivalence.sum_automatas(self.equivalence.automata1, self.equivalence.automata2)
        self.assertTrue(len(self.summedautomata.Q)==7)
        self.assertTrue(len(self.summedautomata.S)==2)
        self.assertTrue(len(self.summedautomata.R)==2)
        astate = self.summedautomata.transition_map['A']
        self.assertTrue(len(astate)==2)
        self.assertTrue(astate[0] == ('a', 'C', 0) or astate[0] == ('b', 'B', 0))

    ##To prove that two automatas are equivalent given the final partition
    def test_validate_equivalence(self):
        self.set_up_validate_equivalence()
        self.assertTrue(self.equivalence.validate_equivalence(self.automata1, self.automata2, self.partitions))

    ##To prove that two automatas are equivalent from scratch 
    def test_are_equivalence(self):
        self.set_up_automata()
        response = self.equivalence.are_equivalent()
        self.assertEquals(response, Equivalence.EQUIVALENT_MACHINES)



       


    

    





