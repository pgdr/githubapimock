import unittest
import githubapimock as mock
from githubapimock import client


class TestClient(unittest.TestCase):
    def setUp(self):
        mock.new()

    def tearDown(self):
        mock.close()

    def test_create_bug(self):
        num = client.create_bug_report('Bug a', 'buggy bugs')
        nums = [x['number'] for x in client.get_column('bug')]
        self.assertIn(num, nums)


if __name__ == '__main__':
    unittest.main()
