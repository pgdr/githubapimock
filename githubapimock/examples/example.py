import requests
import githubapimock

githubapimock.new()

repo = ''
username = ''
token = ''

num = githubapimock.create_issue(repo, username, token, 'A', 'ala')
assert num == 1

issue1 = githubapimock.get_issue(repo, username, token, num)
assert issue1['title'] == 'A'
assert issue1['body'] == 'ala'
assert issue1['user'] == ''
assert issue1['status'] == 'open'
assert issue1['number'] == 1


issues = githubapimock.get_issues(repo, username, token)
assert issue1 in issues


githubapimock.close_issue(repo, username, token, num)

issue1_closed = githubapimock.get_issue(repo, username, token, num)
issue1['status'] = 'closed'
assert issue1_closed == issue1


x = githubapimock.get_issues(repo, username, token)
assert issue1 in x


githubapimock.close()
