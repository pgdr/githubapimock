import os
import githubapimock as api
import yaml

org = 'pgdr'
username = 'pgdr'
token = 'none'
repo = 'githubapimock'

if os.getenv('MOCK'):
    api.new()  # for mocking


issues = yaml.load(open('issues.yml'))

nums = []

for issue in issues:
    num = api.create_issue(
        org=org,
        repo=repo,
        username=username,
        token=token,
        title=issue['title'],
        body=issue['body']
    )
    nums.append(num)


api.set_labels(org=org,
               repo=repo,
               username=username,
               token=token,
               issue_id=nums[0],
               labels=['in progress', 'good first issue', 'help wanted'])

for num in nums[1:]:
    api.set_labels(org=org,
                   repo=repo,
                   username=username,
                   token=token,
                   issue_id=num,
                   labels=['todo', 'enhancement'])
