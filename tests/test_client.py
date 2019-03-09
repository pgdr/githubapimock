import os
import unittest
import githubapimock as mock
from githubapimock import client


class TestClient(unittest.TestCase):
    def setUp(self):
        assert os.getenv('MOCK')
        mock.new()

    def tearDown(self):
        mock.close()


    def test_create_bug(self):
        num = client.create_bug_report('Bug a', 'buggy bugs')
        nums = [x['number'] for x in client.get_column('bug')]
        self.assertIn(num, nums)


    def test_progression_start_bug(self):
        num = client.create_bug_report('Bug a', 'buggy bugs')
        client.start_issue(num)
        self.assertEqual(
            set(['bug', 'in progress']),
            set(client.get_labels(num)))


    def test_progression_reset_feature(self):
        num = client.create_feature_request('Feature a', 'buggy bugs feet')
        client.reset_issue(num)
        self.assertEqual(
            set(['feature', 'backlog']),
            set(client.get_labels(num)))


    def test_progression_advance(self):
        num = client.create_issue('Feature a', 'buggy bugs feet')
        with self.assertRaises(Exception):
            client.advance(num)
        client.start_issue(num)
        self.assertEqual(['in progress'], client.get_labels(num))

        client.advance(num)
        self.assertEqual(['in review'], client.get_labels(num))

        client.advance(num)
        self.assertEqual(['done'], client.get_labels(num))

        with self.assertRaises(Exception):
            client.advance(num)


    def test_state(self):
        num = client.create_issue('Feature a', 'buggy bugs feet')
        state = client.get_state(num)
        self.assertEqual('open', state)

        client.close_issue(num)
        state = client.get_state(num)
        self.assertEqual('closed', state)

        client.set_state(num, 'xyz')
        state = client.get_state(num)
        self.assertEqual('xyz', state)


if __name__ == '__main__':
    unittest.main()
