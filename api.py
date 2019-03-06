import githubapimock as api
import yaml

username = 'pgdr'
token = 'none'
repo = 'githubapimock'

api.new()  # for mocking

issues = yaml.load(open('issues.yml'))

for issue in issues:
    api.create_issue(
        repo=repo,
        username=username,
        token=token,
        title=issue['title'],
        body=issue['body']
    )
