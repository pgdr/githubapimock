import unittest
import githubapimock as mock

repo = ''
username = ''
token = ''

class TestMock(unittest.TestCase):
    def setUp(self):
        mock.new()

    def tearDown(self):
        mock.close()

    def test_create(self):
        num = mock.create_issue(repo, username, token, 'A', 'ala')
        self.assertEqual(num, 1)

    def test_get_issue(self):
        num_1 = mock.create_issue(repo, username, token, 'A', 'ala')
        num_2 = mock.create_issue(repo, username, token, 'B', 'balala')

        issue1 = mock.get_issue(repo, username, token, num_1)
        self.assertEqual(issue1['title'], 'A')
        self.assertEqual(issue1['body'], 'ala')
        self.assertEqual(issue1['user'], '')
        self.assertEqual(issue1['status'], 'open')
        self.assertEqual(issue1['number'], 1)

    def test_get_issues(self):
        num = mock.create_issue(repo, username, token, 'A', 'ala')
        issue1 = mock.get_issue(repo, username, token, num)
        issues = mock.get_issues(repo, username, token)
        self.assertIn(issue1, issues)

    def test_close_issue(self):
        num = mock.create_issue(repo, username, token, 'A', 'ala')
        issue1 = mock.get_issue(repo, username, token, num)
        issues = mock.get_issues(repo, username, token)
        mock.close_issue(repo, username, token, num)
        issue1_closed = mock.get_issue(repo, username, token, num)
        issue1['status'] = 'closed'
        self.assertEqual(issue1_closed, issue1)


if __name__ == '__main__':
    unittest.main()
