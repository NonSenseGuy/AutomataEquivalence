import unittest
import src.Partition

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


    ##To prove the comparision between two states are in the same partition or not 
    def test_same_partition(self):
        self.setup_same_partition()
        self.assertTrue(src.Partition.same_partition(self.partitions, 'A', 'B'))
        self.assertTrue(src.Partition.same_partition(self.partitions, 'C', 'D'))


