from unittest import TestCase
from node import node


class TestNode(TestCase):
    def setUp(self):
        myNode = node(10)
        self.node = myNode

    def testGetData(self):
        data = self.node.getData()
        self.assertEqual(10, data)

    def testSetData(self):
        data = 30
        self.node.setData(data)
        self.assertEqual(data, self.node.getData())

