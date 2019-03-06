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

    def test_progression(self):
        num = client.create_bug_report('Bug a', 'buggy bugs')
        client.start_issue(num)
        self.assertEqual(
            set(['bug', 'in progress']),
            set(client.get_labels(num)))


if __name__ == '__main__':
    unittest.main()
