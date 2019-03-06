from . import _mock as mock

repo = ''
username = ''
token = ''

PROGRESSION = ['backlog', 'todo', 'done']
TICKET_TYPES = ['bug', 'feature', 'epic']

def create_bug_report(title, body):
    num = mock.create_issue(repo, username, token, title, body)
    mock.set_labels(repo, username, token, num, ['bug'])
    return num

def get_column(label):
    issues = mock.get_issues(repo, username, token)
    for issue in issues:
        num = issue['number']
        labs = mock.get_labels(repo, username, token, num)
        if label in labs:
            yield issue
