import glob
import json
import logging
import os
import unittest

from server import create_app

log = logging.getLogger(__name__)


class Histogram(unittest.TestCase):

    endpoint = '/api/1/example/'

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_01_histogram_get(self):
        """Test API can get example (GET request)"""
        print("====================== test_01_example_get ======================")
        res = self.client().get(self.endpoint)
        self.assertEqual(res.status_code, 200)

    def test_02_example_snapshots(self):
        # """Test API return data matches snapshot (GET request)"""
        print("====================== test_02_example_snapshots ======================")
        path = os.path.dirname(os.path.realpath(__file__))
        snapshots = os.path.join(path, '__snapshots__/example/')
        for snap in glob.glob(snapshots):
            results = {}

            results_path = os.path.join(snap, 'example.json')
            with open(results_path, 'r') as f:
                results = json.load(f)

            res = self.client().get(self.endpoint)
            self.assertEqual(res.status_code, 200)

            data = res.get_json()
            self.assertEqual(data, results)


if __name__ == '__main__':
    unittest.main()
