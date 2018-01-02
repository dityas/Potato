import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.datastruct import *
from potato.backend import *

class TestFrame(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects/Experiment_Results"
        self.files=get_data_files(self.path,["ztomatrix.txt"])
        self.streamer=Streamer(self.files)
        self.frame=Frame(self.streamer)

    def test_frame_creation(self):
        self.assertIsNotNone(self.frame)

    def test_frame_head(self):
        self.assertEqual(len(self.frame.head(5)),5)
