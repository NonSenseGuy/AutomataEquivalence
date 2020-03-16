import unittest
import src.Partition
from MealyAutomata import MealyAutomata
from Automata import Automata

class Partition_Test(unittest.TestCase):

    def setup_same_partition(self):
        self.partitions = []
        self.partition = set()
        self.partition.add('A')
        self.partition.add('B')
        self.partitions.append(self.partition)
        self.partition = set()
        self.partition.add('C')
        self.partition.add('D')
        self.partitions.append(self.partition)

    def set_up_automata(self):
        self.automata = MealyAutomata(['A', 'B', 'C', 'W', 'X', 'Y', 'Z'], ['a','b'], [0,1], 'A')
        self.automata.add_state('B')
        self.automata.add_state('C')
        self.automata.add_state('W')
        self.automata.add_state('X')
        self.automata.add_state('Y')
        self.automata.add_state('Z')
        self.automata.add_transition('a', 'A', 'C', 0)
        self.automata.add_transition('a', 'B', 'C', 0)
        self.automata.add_transition('a', 'C', 'B', 0)
        self.automata.add_transition('a', 'W', 'Z', 0)
        self.automata.add_transition('a', 'X', 'Z', 0)
        self.automata.add_transition('a', 'Y', 'Z', 0)
        self.automata.add_transition('a', 'Z', 'Y', 0)
        self.automata.add_transition('b', 'A', 'B', 0)
        self.automata.add_transition('b', 'B', 'A', 1)
        self.automata.add_transition('b', 'C', 'C', 0)
        self.automata.add_transition('b', 'W', 'X', 0)
        self.automata.add_transition('b', 'X', 'W', 1)
        self.automata.add_transition('b', 'Y', 'W', 1)
        self.automata.add_transition('b', 'Z', 'Z', 0)

        self.firstpartition=[]
        self.partition = set()
        self.partition.add('A')
        self.partition.add('C')
        self.partition.add('W')
        self.partition.add('Z')
        self.firstpartition.append(self.partition)
        self.partition = set()
        self.partition.add('B')
        self.partition.add('X')
        self.partition.add('Y')
        self.firstpartition.append(self.partition)

    def set_up_first_partition_states(self):
        self.set_up_automata()
        self.partition1 = set()
        self.partition1.add('A')
        self.partition1.add('C')
        self.partition1.add('W')
        self.partition1.add('Z')

    def set_up_first_partition_states2(self):
        self.set_up_automata()
        self.partition1 = set()
        self.partition1.add('B')
        self.partition1.add('X')
        self.partition1.add('Y')

    ##To prove the comparision between two states are in the same partition or not 
    def test_same_partition(self):
        self.setup_same_partition()
        self.assertTrue(src.Partition.same_partition(self.partitions, 'A', 'B'))
        self.assertFalse(src.Partition.same_partition(self.partitions, 'A', 'D'))

    ##To prove that two states belongs to the same partition or not
    def test_review_states(self):
        self.set_up_automata()
        self.assertTrue(src.Partition.review_states('A', 'W', self.automata, self.firstpartition))
        self.assertFalse(src.Partition.review_states('A', 'C', self.automata, self.firstpartition))


    def test_same_partition_states(self):
        self.set_up_first_partition_states()
        self.the_states=  src.Partition.same_partition_states(self.partition1, self.firstpartition, self.automata)
        self.assertIn('C', self.the_states)
        self.assertIn('Z', self.the_states)
        self.assertTrue(len(self.the_states)==2)

        self.set_up_first_partition_states2()
        self.the_states=  src.Partition.same_partition_states(self.partition1, self.firstpartition, self.automata)
        self.assertIn('B', self.the_states)
        self.assertIn('X', self.the_states)
        self.assertTrue(len(self.the_states)==3)

    def test_review_partition(self):
        self.set_up_first_partition_states()
        self.partitions = src.Partition.review_partition(self.partition1, self.firstpartition, self.automata)
        self.assertTrue(len(self.partitions)==2)
        self.assertTrue(len(self.partitions[0])==2)
        self.assertTrue(len(self.partitions[1])==2)

        self.set_up_first_partition_states2()
        self.partitions = src.Partition.review_partition(self.partition1, self.firstpartition, self.automata)
        self.assertTrue(len(self.partitions)==1)
        self.assertTrue(len(self.partitions[0])==3)

    
    

    





