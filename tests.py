import os
import unittest

path = os.path.dirname(os.path.abspath(__file__))
start_dir = os.path.join(path, 'tests')

loader = unittest.TestLoader()
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
