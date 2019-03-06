from pprint import pprint
import requests
import githubapimock

username = 'pgdr'
token = 'none'
repo = 'githubapimock'


githubapimock.new()  # for mocking

num_1 = githubapimock.create_issue(repo, username, token, 'Xyz', 'xyz')
num_2 = githubapimock.create_issue(repo, username, token, 'Omg', 'omg')

issues = githubapimock.get_issues(repo, username, token)
pprint(issues)

githubapimock.close()  # for mocking
