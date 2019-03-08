import requests

URL = 'https://api.github.com/repos/{org}/{repo}/issues'


def create_issue(org, repo, username, token, title, body) -> int:
    payload = {'title': title, 'body': body}
    url = URL.format(org=org, repo=repo)
    resp = requests.post(url, auth=(username, token), json=payload)
    resp.raise_for_status()
    return resp.json()['number']


def close_issue(org, repo, username, token, issue_id):
    url = URL.format(org=org, repo=repo) + "/" + str(issue_id)
    payload = { 'state': 'closed' }
    resp = requests.patch(url, auth=(username, token), json=payload)
    resp.raise_for_status()


def get_issue(org, repo, username, token, issue_id) -> dict:
    url = URL.format(org=org, repo=repo) + '/' + str(issue_id)
    resp = requests.get(url, auth=(username, token))
    resp.raise_for_status()
    return resp.json()


def get_issues(org, repo, username, token):
    url = URL.format(org=org, repo=repo)
    resp = requests.get(url, auth=(username, token))
    resp.raise_for_status()
    return resp.json()


def get_labels(org, repo, username, token, issue_id):
    issue = get_issue(org, repo, username, token, issue_id)
    return [ label['name'] for label in issue['labels'] ]


def set_labels(org, repo, username, token, issue_id, labels:list):
    url = URL.format(org=org, repo=repo) + "/" + str(issue_id)
    payload = { 'labels': labels }
    resp = requests.patch(url, auth=(username, token), json=payload)
    resp.raise_for_status()
