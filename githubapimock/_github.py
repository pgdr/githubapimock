import requests

URL = 'https://api.github.com/repos/pgdr/{repo}/issues'


def create_issue(repo, username, token, title, body) -> int:
    payload = {'title': title, 'body': body}

    url = URL.format(repo=repo)
    resp = requests.post(url, auth=(username, token), json=payload)
    return resp.json()['number']


def close_issue(repo, username, token, issue_id):
    url = URL.format(repo=repo) + "/" + str(issue_id)
    payload = { 'state': 'closed' }
    requests.patch(url, auth=(username, token), json=payload)


def get_issue(repo, username, token, issue_id) -> dict:
    url = URL.format(repo=repo) + '/' + str(issue_id)
    resp = requests.get(url, auth=(username, token))
    return resp.json()


def get_issues(repo, username, token):
    url = URL.format(repo=repo)
    resp = requests.get(url, auth=(username, token))
    return resp.json()


def get_labels(repo, username, token, issue_id):
    issue = get_issue(repo, username, token, issue_id)
    return [ label['name'] for label in issue['labels'] ]


def set_labels(repo, username, token, issue_id, labels:list):
    pass
