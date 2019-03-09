import os
import unittest
import githubapimock as mock

org = ''
repo = ''
username = ''
token = ''

class TestMock(unittest.TestCase):
    def setUp(self):
        assert os.getenv('MOCK')
        mock.new()

    def tearDown(self):
        mock.close()

    def test_create(self):
        num = mock.create_issue(org, repo, username, token, 'A', 'ala')
        self.assertTrue(num >= 0)  # just testing int

    def test_get_issue(self):
        num_1 = mock.create_issue(org, repo, username, token, 'A', 'ala')
        num_2 = mock.create_issue(org, repo, username, token, 'B', 'balala')

        issue1 = mock.get_issue(org, repo, username, token, num_1)
        self.assertEqual(issue1['title'], 'A')
        self.assertEqual(issue1['body'], 'ala')
        self.assertEqual(issue1['user'], '')
        self.assertEqual(issue1['state'], 'open')
        self.assertEqual(issue1['number'], num_1)

    def test_get_issues(self):
        num = mock.create_issue(org, repo, username, token, 'A', 'ala')
        issue1 = mock.get_issue(org, repo, username, token, num)
        issues = mock.get_issues(org, repo, username, token)
        self.assertIn(issue1, issues)

    def test_close_issue(self):
        num = mock.create_issue(org, repo, username, token, 'A', 'ala')
        issue1 = mock.get_issue(org, repo, username, token, num)
        issues = mock.get_issues(org, repo, username, token)
        mock.close_issue(org, repo, username, token, num)
        issue1_closed = mock.get_issue(org, repo, username, token, num)
        issue1['state'] = 'closed'
        self.assertEqual(issue1_closed, issue1)


    def test_label_issue(self):
        num = mock.create_issue(org, repo, username, token, 'A', 'ala')
        lab_exp = ['lab1', 'lab2']
        mock.set_labels(org, repo, username, token, num, lab_exp)

        lab_act = mock.get_labels(org, repo, username, token, num)
        self.assertEqual(lab_exp, lab_act)

        mock.set_labels(org, repo, username, token, num, ['only'])
        only = mock.get_labels(org, repo, username, token, num)
        self.assertEqual(only, ['only'])


    def test_labels_in_issues(self):
        num = mock.create_issue(org, repo, username, token, 'A', 'ala')
        lab_exp = ['lab1', 'lab2']
        mock.set_labels(org, repo, username, token, num, lab_exp)

        issue = mock.get_issue(org, repo, username, token, num)
        lab_act = [label['name'] for label in issue['labels']]

        self.assertEqual(lab_exp, lab_act)


    def test_issue_get_state(self):
        num_1 = mock.create_issue(org, repo, username, token, 'A', 'ala')
        num_2 = mock.create_issue(org, repo, username, token, 'B', 'balala')

        issue1 = mock.get_issue(org, repo, username, token, num_1)
        self.assertEqual(issue1['title'], 'A')
        self.assertEqual(issue1['body'], 'ala')
        self.assertEqual(issue1['user'], '')
        self.assertEqual(issue1['state'], 'open')
        self.assertEqual(issue1['number'], num_1)

        state = mock.get_state(org, repo, username, token, num_1)
        self.assertEqual(state, 'open')


        mock.set_state(org, repo, username, token, num_1, 'test_set_state')
        state = mock.get_state(org, repo, username, token, num_1)
        self.assertEqual(state, 'test_set_state')


if __name__ == '__main__':
    unittest.main()
